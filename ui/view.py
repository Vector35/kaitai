from typing import Optional

from binaryninja import BinaryView
from binaryninjaui import View, ViewType, ViewFrame, UIContext, HexEditor, getMonospaceFont

import binaryninjaui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QGroupBox, QTreeWidget, QTreeWidgetItem, QLineEdit, \
    QHeaderView, QSplitter

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
            #log_debug('visibleRows=%d, rowCapacity=%d len(queue)=%d' % (visibleRows, rowCapacity, len(queue)))
            if not queue:
                break

            item = queue[0]
            queue = queue[1:]

            if not item.isExpanded():
                item.setExpanded(True)
                for i in range(item.childCount()):
                    queue.append(item.child(i))
                    visibleRows += 1


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

        # splitter = top half, bottom half
        self.splitter = QSplitter(self)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.addWidget(topHalf)
        self.splitter.addWidget(self.hex_widget)

        self.setWidgetResizable(True)
        self.setWidget(self.splitter)

        self.construct_view()

    # parse the file using Kaitai, construct the TreeWidget
    def construct_view(self, module_name: Optional[str] = None):
        bv = self.binary_view
        if self.binary_view.length == 0:
            return

        if not module_name:
            data_sample = bv.read(0, 16)
            # TODO: Remove len check here.
            if len(data_sample) == 16:
                module_name = kshelpers.infer_kaitai_module(data_sample, bv.length, bv.file.filename)

        io_view = kshelpers.KaitaiBinaryViewIO(self.binary_view)
        kt_struct = kshelpers.parse_io_view(io_view, module_name)
        if not kt_struct:
            return

        tree = kshelpers.build_tree(kt_struct)

        def convert(node, parent=None):
            start_str = 'None' if node.start is None else f'{node.start:08X}'
            end_str = 'None' if node.end is None else f'{node.end:08X}'

            result = QTreeWidgetItem(parent, [str(node.name), str(node.value), start_str, end_str])
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
        UIContext.updateStatus(True)

    def getFont(self):
        return binaryninjaui.getMonospaceFont(self)

    def navigate(self, addr):
        self.root_selection_start = addr
        self.root_selection_end = addr + 1
        self.hex_widget.setSelectionOffsets((addr, addr + 1))
        return True

    def navigateToFileOffset(self, offset):
        return False

    def onTreeSelect(self, wtf=None):
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

        #
        start, end = int(item.text(2), 16), int(item.text(3), 16)
        if start == None or end == None:
            return

        self.root_selection_start = start
        self.root_selection_end = end

        self.hex_widget.setSelectionOffsets((start, end - start))

        return

        # determine current IO we're in (the Kaitai input/output abstraction)
        _io = None
        # if the tree item is linked to a KaitaiNode, simply read the IO
        if item.kt_struct:
            _io = item.kt_struct._parent._io
        else:
            # else we're a leaf
            parent = item.parent()
            if parent:
                # a leaf with a parent -> read parent's IO
                _io = parent.kt_struct._io
            else:
                # a leaf without a parent -> we must be at root -> use root IO
                _io = self.ioRoot

        # if the selection is in the root view, store the interval so that upon
        # getCurrentOffset() callback, we return the middle and feature map is
        # updated
        if _io == self.ioRoot:
            self.root_selection_start = start
            self.root_selection_end = end

        # current kaitai object is on a different io? then swap HexEditor
        if _io != self.ioCurrent:
            # delete old view
            self.hex_widget.hide()
            self.hex_widget.setParent(None)
            self.hex_widget.deleteLater()
            self.hex_widget = None

            # if it's the original file IO, wrap the already-open file binary view
            if _io == self.ioRoot:
                self.hex_widget = HexEditor(self.binary_view, ViewFrame.viewFrameForWidget(self), 0)
            # otherwise delete old view, create a temporary view
            else:
                # create new view
                length = _io.size()
                _io.seek(0)
                data = _io.read_bytes(length)
                bv = BinaryView.new(data)
                self.hex_widget = HexEditor(bv, ViewFrame.viewFrameForWidget(self), 0)

            self.splitter.addWidget(self.hex_widget)
            self.ioCurrent = _io

        # now position selection in whatever HexEditor is current
        self.hex_widget.setSelectionOffsets((start, end))

        # TODO: set hex group title to reflect current selection
        #self.hexGroup.setTitle('Hex View @ [0x%X, 0x%X)' % (start, end))

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