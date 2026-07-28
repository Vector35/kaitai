from typing import Optional

from binaryninja import BinaryView
from binaryninjaui import View, ViewType, ViewFrame, UIContext, HexEditor, getMonospaceFont

import binaryninjaui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QTreeWidget, QTreeWidgetItem, \
    QLineEdit, QHeaderView, QSplitter, QPlainTextEdit, QPushButton, QLabel, QFileDialog

from .. import kshelpers
from . import menu

class MyQTreeWidget(QTreeWidget):
    def __init__(self):
        QTreeWidget.__init__(self)

        self.old_width = 0
        self.old_height = 0

        self.queue_initial_presentation = False

    def resizeEvent(self, event):
        QTreeWidget.resizeEvent(self, event)

        if self.queue_initial_presentation:
            self.initialPresentation()

        self.scrollTo(self.currentIndex())

        new_width = self.width()
        new_height = self.height()

        if new_width == self.old_width and new_height == self.old_height:
            return

        self.old_width = new_width
        self.old_height = new_height

        self.set_column_widths()

    def initialPresentation(self):
        self.initial_expand()

        if self.topLevelItemCount():
            self.topLevelItem(0).setSelected(True)

        self.queue_initial_presentation = False

    def set_column_widths(self):
        width = self.width()
        self.setColumnWidth(0, .6 * width)
        self.setColumnWidth(1, .2 * width)
        self.setColumnWidth(2, .1 * width)
        self.setColumnWidth(3, .1 * width)

    def initial_expand(self):
        visibleRows = self.topLevelItemCount()
        if not visibleRows:
            return

        height = self.height()
        rowHeight = self.visualItemRect(self.topLevelItem(0)).height()
        rowCapacity = height / rowHeight

        queue = []
        for i in range(visibleRows):
            queue.append(self.topLevelItem(i))

        while visibleRows < rowCapacity:
            if not queue:
                break

            item = queue[0]
            queue = queue[1:]

            if not item.isExpanded():
                item.setExpanded(True)
                for i in range(item.childCount()):
                    queue.append(item.child(i))
                    visibleRows += 1


# sorts the start/end (hex) columns numerically rather than lexicographically,
# so values don't need to be zero-padded for display
class KaitaiTreeWidgetItem(QTreeWidgetItem):
    def __lt__(self, other):
        tree = self.treeWidget()
        col = tree.sortColumn() if tree else 0
        if col in (2, 3):
            return self._num(col) < other._num(col)
        return self.text(col) < other.text(col)

    def _num(self, col):
        try:
            return int(self.text(col), 16)
        except ValueError:
            return -1


class KaitaiView(QScrollArea, View):
    def __init__(self, parent, binary_view: BinaryView):
        QScrollArea.__init__(self, parent)

        View.__init__(self)
        View.setBinaryDataNavigable(self, True)
        self.setupView(self)

        self.binary_view = binary_view

        self.root_selection_start = 0
        self.root_selection_end = 1

        self.ioRoot = None
        self.ioCurrent = None

        # (start, end, QTreeWidgetItem) per node, for hex->tree lookup
        self.node_intervals = []
        # guard against tree<->hex selection feedback loops
        self._syncing = False

        # active-format tracking
        self.ksy_path = None         # file the editor is bound to (None = unsaved)
        self.active_name = None      # format name currently driving the tree
        self.active_source = None    # 'builtin' | 'file' | 'editor'
        self.compiled_text = None    # editor text at last successful compile
        self.editor_locked = True    # editor read-only by default

        # top half = treeWidget + structPath
        self.tree_widget = MyQTreeWidget()
        self.tree_widget.setColumnCount(4)
        self.tree_widget.setHeaderLabels(['label', 'value', 'start', 'end'])
        self.tree_widget.itemSelectionChanged.connect(self.onTreeSelect)

        self.struct_path = QLineEdit("root")
        self.struct_path.setReadOnly(True)

        topHalf = QWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(self.tree_widget)
        layout.addWidget(self.struct_path)
        topHalf.setLayout(layout)

        # bottom half = hexWidget
        self.hex_widget = HexEditor(binary_view, ViewFrame.viewFrameForWidget(self), 0)

        # editor pane = active-format line + .ksy editor + buttons + sync/status line
        self.active_label = QLabel('', self)

        self.ksy_editor = QPlainTextEdit(self)
        self.ksy_editor.setFont(binaryninjaui.getMonospaceFont(self))
        self.ksy_editor.setPlaceholderText('Load or write a Kaitai .ksy here, then Compile && Parse')
        self.ksy_editor.textChanged.connect(self.refresh_indicators)

        self.ksy_lock_btn = QPushButton(self)
        self.ksy_lock_btn.setCheckable(True)
        self.ksy_lock_btn.clicked.connect(self.on_lock_toggled)
        self.ksy_load_btn = QPushButton('Load…', self)
        self.ksy_load_btn.clicked.connect(self.on_load_clicked)
        self.ksy_save_btn = QPushButton('Save', self)
        self.ksy_save_btn.clicked.connect(self.on_save_clicked)
        self.ksy_compile_btn = QPushButton('Compile && Parse', self)
        self.ksy_compile_btn.clicked.connect(self.on_compile_clicked)

        buttonRow = QHBoxLayout()
        buttonRow.addWidget(self.ksy_lock_btn)
        buttonRow.addWidget(self.ksy_load_btn)
        buttonRow.addWidget(self.ksy_save_btn)
        buttonRow.addWidget(self.ksy_compile_btn)

        self.sync_label = QLabel('', self)
        self.ksy_status = QLabel('', self)
        statusRow = QHBoxLayout()
        statusRow.addWidget(self.sync_label)
        statusRow.addWidget(self.ksy_status)
        statusRow.addStretch(1)

        editorPane = QWidget(self)
        editorLayout = QVBoxLayout()
        editorLayout.addWidget(self.active_label)
        editorLayout.addWidget(self.ksy_editor)
        editorLayout.addLayout(buttonRow)
        editorLayout.addLayout(statusRow)
        editorPane.setLayout(editorLayout)

        self.set_locked(True)

        # splitter = tree, hex, editor
        self.splitter = QSplitter(self)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.addWidget(topHalf)
        self.splitter.addWidget(self.hex_widget)
        self.splitter.addWidget(editorPane)

        self.setWidgetResizable(True)
        self.setWidget(self.splitter)

        self.construct_view()

    # parse the file using Kaitai, construct the TreeWidget
    # pass ks_class to parse with a specific (e.g. live-compiled) class instead of inferring
    def construct_view(self, module_name: Optional[str] = None, ks_class=None):
        bv = self.binary_view
        if self.binary_view.length == 0:
            return False

        io_view = kshelpers.KaitaiBinaryViewIO(self.binary_view)

        if ks_class is not None:
            kt_struct = kshelpers.parse_io_view_with_class(io_view, ks_class)
        else:
            if not module_name:
                data_sample = bv.read(0, 16)
                # TODO: Remove len check here.
                if len(data_sample) == 16:
                    module_name = kshelpers.infer_kaitai_module(data_sample, bv.length, bv.file.filename)
            kt_struct = kshelpers.parse_io_view(io_view, module_name)

        if not kt_struct:
            return False

        tree = kshelpers.build_tree(kt_struct)

        self.node_intervals = []

        def convert(node, parent=None):
            start_str = '' if node.start is None else f'0x{node.start:X}'
            end_str = '' if node.end is None else f'0x{node.end:X}'
            value_str = '' if node.value is None else str(node.value)

            result = KaitaiTreeWidgetItem(parent, [str(node.name), value_str, start_str, end_str])
            if node.start is not None and node.end is not None and node.end > node.start:
                self.node_intervals.append((node.start, node.end, result))
            for child in node.children:
                convert(child, result)
            return result

        qwi = convert(tree)

        io_view.seek(0)
        self.ioRoot = io_view
        self.ioCurrent = io_view

        self.tree_widget.clear()
        self.tree_widget.setSortingEnabled(False)  # temporarily, for efficiency

        self.tree_widget.insertTopLevelItems(0, qwi.takeChildren())

        # enable sorting
        self.tree_widget.setSortingEnabled(True)
        self.tree_widget.sortByColumn(2, Qt.AscendingOrder)

        # TODO: select first item, maybe expand a few things
        self.root_selection_start = 0
        self.root_selection_end = 1

        self.tree_widget.setUniformRowHeights(True)
        self.tree_widget.queue_initial_presentation = True

        # a built-in/auto-detected format drove this parse; the editor isn't the
        # source of truth, so mark it active and lock the editor by default
        if ks_class is None:
            self.set_active(module_name, 'builtin')
            self.set_locked(True)

        return True

    def getData(self):
        return self.binary_view

    def getStart(self):
        return self.binary_view.start

    def getEnd(self):
        return self.binary_view.end

    def getLength(self):
        return self.binary_view.length

    def getCurrentOffset(self):
        return self.root_selection_start

    def getSelectionOffsets(self):
        if self.hex_widget:
            result = self.hex_widget.getSelectionOffsets()
        else:
            result = (self.root_selection_start, self.root_selection_start)
        return result

    def setCurrentOffset(self, offset):
        self.root_selection_start = offset
        self.root_selection_end = offset + 1
        self.select_tree_node_for_offset(offset)
        UIContext.updateStatus(True)

    def getFont(self):
        return binaryninjaui.getMonospaceFont(self)

    def navigate(self, addr):
        self.root_selection_start = addr
        self.root_selection_end = addr + 1
        self.hex_widget.setSelectionOffsets((addr, addr + 1))
        # hex/global navigation (e.g. clicking a byte) propagates here -> sync tree
        self.select_tree_node_for_offset(addr)
        return True

    # hex -> tree: select the smallest parsed region containing this file offset
    def select_tree_node_for_offset(self, offset):
        if self._syncing:
            return

        best_item = None
        best_size = None
        for start, end, item in self.node_intervals:
            if start <= offset < end:
                size = end - start
                if best_size is None or size < best_size:
                    best_item, best_size = item, size

        if best_item is None:
            return

        self._syncing = True
        try:
            parent = best_item.parent()
            while parent:
                parent.setExpanded(True)
                parent = parent.parent()
            self.tree_widget.setCurrentItem(best_item)
            self.tree_widget.scrollToItem(best_item)
        finally:
            self._syncing = False

    # editor lock (write protection)
    def set_locked(self, locked):
        self.editor_locked = locked
        self.ksy_editor.setReadOnly(locked)
        self.ksy_lock_btn.setChecked(locked)
        self.ksy_lock_btn.setText('🔒 Locked' if locked else '🔓 Editable')
        self.refresh_indicators()

    def on_lock_toggled(self):
        self.set_locked(self.ksy_lock_btn.isChecked())

    # record which format is currently driving the tree view
    def set_active(self, name, source):
        self.active_name = name
        self.active_source = source
        self.refresh_indicators()

    # update the "which format is active" and "edits compiled?" indicators
    def refresh_indicators(self):
        if not self.active_name:
            self.active_label.setText('Active format: (none — open a file or compile a .ksy)')
        elif self.active_source == 'builtin':
            self.active_label.setText(f'Active format: {self.active_name}  ·  built-in')
        elif self.active_source == 'file':
            self.active_label.setText(f'Active format: {self.active_name}  ·  {self.ksy_path or "file"}')
        else:
            self.active_label.setText(f'Active format: {self.active_name}  ·  editor')

        # sync indicator: relationship between editor text and what was last compiled
        text = self.ksy_editor.toPlainText()
        if not text.strip():
            self.sync_label.setText('')
        elif self.compiled_text is None:
            self.sync_label.setText('○ not compiled')
        elif text == self.compiled_text:
            self.sync_label.setText('✓ up to date')
        else:
            self.sync_label.setText('● modified — recompile to apply')

    # load a .ksy from disk into the editor and remember its path
    def on_load_clicked(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Load Kaitai format', self.ksy_path or '',
                                              'Kaitai struct (*.ksy);;All files (*)')
        if not path:
            return
        try:
            with open(path, 'r') as fp:
                self.ksy_editor.setPlainText(fp.read())
        except OSError as e:
            self.ksy_status.setText(f'✗ {e}')
            return
        self.ksy_path = path
        self.compiled_text = None  # freshly loaded, not yet compiled
        self.set_locked(False)     # the user is editing this file
        self.ksy_status.setText(f'loaded {path}')

    # save the editor contents; save directly if loaded from a file, else prompt
    def on_save_clicked(self):
        path = self.ksy_path
        if not path:
            path, _ = QFileDialog.getSaveFileName(self, 'Save Kaitai format', '',
                                                  'Kaitai struct (*.ksy);;All files (*)')
            if not path:
                return
        try:
            with open(path, 'w') as fp:
                fp.write(self.ksy_editor.toPlainText())
        except OSError as e:
            self.ksy_status.setText(f'✗ {e}')
            return
        self.ksy_path = path
        self.ksy_status.setText(f'saved {path}')

    # compile the .ksy in the editor pane and reparse the current file with it
    def on_compile_clicked(self):
        source = self.ksy_editor.toPlainText()
        if not source.strip():
            self.ksy_status.setText('(empty .ksy)')
            return
        try:
            module_path, module_name, class_name = kshelpers.compile_ksy(source)
            ks_class = kshelpers.load_ksy_class(module_path, module_name, class_name)
        except Exception as e:
            self.ksy_status.setText(f'✗ {e}')
            return
        if not self.construct_view(ks_class=ks_class):
            self.ksy_status.setText(f'✗ {module_name} compiled but did not parse this file')
            return
        # the editor is now the source of truth for the active format
        self.compiled_text = source
        self.set_active(module_name, 'file' if self.ksy_path else 'editor')
        self.ksy_status.setText(f'✓ {module_name}.{class_name} compiled and parsed')

    def navigateToFileOffset(self, offset):
        return False

    def onTreeSelect(self, wtf=None):
        # ignore selections we triggered ourselves from a hex->tree sync
        if self._syncing:
            return

        # get KaitaiTreeWidgetItem
        items = self.tree_widget.selectedItems()
        if not items or len(items) < 1:
            return
        item = items[0]

        # build path, inform user
        structPath = item.text(0)
        itemTmp = item
        while itemTmp.parent():
            itemTmp = itemTmp.parent()
            label = itemTmp.text(0)
            if label.startswith('_m_'):
                label = label[3:]
            structPath = label + '.' + structPath
        self.struct_path.setText('root.' + structPath)

        # offset columns may be blank for fields without a byte range
        try:
            start, end = int(item.text(2), 16), int(item.text(3), 16)
        except ValueError:
            return

        self.root_selection_start = start
        self.root_selection_end = end

        self.hex_widget.setSelectionOffsets((start, end))

    def getHeaderOptionsWidget(self):
        return menu.KaitaiOptionsWidget(self)


class KaitaiViewType(ViewType):
    def __init__(self):
        ViewType.__init__(self, "Kaitai", "Kaitai")

    def getPriority(self, bv: BinaryView, filename):
        # executable means the view is mapped like an OS loader would load an executable (eg: view=ELF)
        # !executable means executable image is not mapped (eg: view=Raw) (or something like .png is loaded)
        if bv.executable:
            return 0

        if bv.start != 0:
            return 1

        data_sample = bv.read(0, 16)
        if len(data_sample) != 16:
            return 1

        # if we don't recognize it, return 1
        module_name = kshelpers.infer_kaitai_module(data_sample, bv.length, filename)
        if not module_name:
            return 1

        # for executables, yield to triage (25)
        if module_name in ['elf', 'microsoft_pe', 'mach_o']:
            return 24

        #
        return 100

    def create(self, binary_view: BinaryView, view_frame: ViewFrame):
        return KaitaiView(view_frame, binary_view)