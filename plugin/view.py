# -*- coding: utf-8 -*-

# python stuff
import io
import os
import sys
import types
import inspect
import traceback

# binja stuff
from binaryninja.log import log_debug, log_info, log_error
from binaryninja import binaryview
from binaryninja.settings import Settings
from binaryninja import _binaryninjacore as core
from binaryninjaui import View, ViewType, ViewFrame, UIContext, HexEditor, getMonospaceFont

import binaryninjaui
if "qt_major_version" in dir(binaryninjaui) and binaryninjaui.qt_major_version == 6:
        from PySide6.QtCore import Qt
        from PySide6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QGroupBox, QTreeWidget, QTreeWidgetItem, QLineEdit, QHeaderView, QSplitter
else:
        from PySide2.QtCore import Qt
        from PySide2.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QGroupBox, QTreeWidget, QTreeWidgetItem, QLineEdit, QHeaderView, QSplitter

#

import kshelpers
from . import menu

class MyQTreeWidget(QTreeWidget):
    def __init__(self):
        QTreeWidget.__init__(self)

        self.oldWidth = 0
        self.oldHeight = 0

        self.queueInitialPresentation = False

    def resizeEvent(self, event):
        QTreeWidget.resizeEvent(self, event)

        if self.queueInitialPresentation:
            self.initialPresentation()

        self.scrollTo(self.currentIndex())

        newWidth = self.width()
        newHeight = self.height()

        #log_debug('QTreeWidget resizeEvent(), now I\'m %dx%d' % (newWidth, newHeight))

        if newWidth == self.oldWidth and newHeight == self.oldHeight:
            return

        self.oldWidth = newWidth
        self.oldHeight = newHeight

        self.setColumnWidthsNicely()

    def initialPresentation(self):
        self.expandNicely()

        if self.topLevelItemCount():
            self.topLevelItem(0).setSelected(True)

        self.queueInitialPresentation = False

    def setColumnWidthsNicely(self):
        width = self.width()
        self.setColumnWidth(0, .6*width)
        self.setColumnWidth(1, .2*width)
        self.setColumnWidth(2, .1*width)
        self.setColumnWidth(3, .1*width)

    def expandNicely(self):
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
    def __init__(self, parent, binaryView):
        QScrollArea.__init__(self, parent)

        View.__init__(self)
        View.setBinaryDataNavigable(self, True)
        self.setupView(self)

        # BinaryViewType
        self.binaryView = binaryView

        self.rootSelectionStart = 0
        self.rootSelectionEnd = 1

        self.ioRoot = None
        self.ioCurrent = None

        # top half = treeWidget + structPath
        self.treeWidget = MyQTreeWidget()
        self.treeWidget.setColumnCount(4)
        self.treeWidget.setHeaderLabels(['label','value','start','end'])
        self.treeWidget.itemSelectionChanged.connect(self.onTreeSelect)

        self.structPath = QLineEdit("root")
        self.structPath.setReadOnly(True)

        topHalf = QWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(self.treeWidget)
        layout.addWidget(self.structPath)
        topHalf.setLayout(layout)

        # bottom half = hexWidget
        self.hexWidget = HexEditor(binaryView, ViewFrame.viewFrameForWidget(self), 0)

        # splitter = top half, bottom half
        self.splitter = QSplitter(self)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.addWidget(topHalf)
        self.splitter.addWidget(self.hexWidget)

        self.setWidgetResizable(True)
        self.setWidget(self.splitter)

        self.kaitaiParse()

    # parse the file using Kaitai, construct the TreeWidget
    def kaitaiParse(self, ksModuleName=None):
        #log_debug(f'INFO: kaitaiParse({ksModuleName}) with len(bv)={len(self.binaryView)} and bv.file.filename={self.binaryView.file.filename}')

        bv = self.binaryView
        if bv.length == 0:
            return

        if not ksModuleName:
            dataSample = bv.read(0, 16)
            if len(dataSample) == 16:
                ksModuleName = kshelpers.infer_kaitai_module(dataSample, bv.length, bv.file.filename)

        kaitaiIO = kshelpers.KaitaiBinaryViewIO(self.binaryView)
        ksobj = kshelpers.parseIo(kaitaiIO, ksModuleName)
        if not ksobj:
            return

        #print(f'INFO: building tree on {ksobj}')
        tree = kshelpers.build_tree(ksobj)

        def convert(node, parent=None):
            start_str = 'None' if node.start == None else f'{node.start:08X}'
            end_str = 'None' if node.end == None else f'{node.end:08X}'

            result = QTreeWidgetItem(parent, [str(node.name), str(node.value), start_str, end_str])
            for child in node.children:
                convert(child, result)
            return result

        qwi = convert(tree)

        kaitaiIO.seek(0)
        self.ioRoot = kaitaiIO
        self.ioCurrent = kaitaiIO

        self.treeWidget.clear()
        self.treeWidget.setSortingEnabled(False)                        # temporarily, for efficiency

        self.treeWidget.insertTopLevelItems(0, qwi.takeChildren())

        # enable sorting
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.sortByColumn(2, Qt.AscendingOrder)

        # TODO: select first item, maybe expand a few things
        self.rootSelectionStart = 0
        self.rootSelectionEnd = 1

        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.queueInitialPresentation = True

    # binja callbacks
    def getData(self):
        return self.binaryView

    def getStart(self):
        result = self.binaryView.start
        #log_debug('getStart() returning '+str(result))
        return result

    def getEnd(self):
        result = self.binaryView.end
        #log_debug('getEnd() returning '+str(result))
        return result

    def getLength(self):
        result = self.binaryView.length
        #log_debug('getLength() returning '+str(result))
        return result

    def getCurrentOffset(self):
        if True:
            # aim at start of selected region
            result = self.rootSelectionStart
        else:
            # aim at midpoint of selected region
            result = self.rootSelectionStart + int((self.rootSelectionEnd - self.rootSelectionStart)/2)

        #print(f'INFO: getCurrentOffset() returning {result:08X}')
        return result

    def getSelectionOffsets(self):
        result = None
        if self.hexWidget:
            result = self.hexWidget.getSelectionOffsets()
        else:
            result = (self.rootSelectionStart, self.rootSelectionStart)
        #print(f'INFO: getSelectionOffsets() returning ({result[0]:08X}, {result[1]:08X})')
        return result

    def setCurrentOffset(self, offset):
        #print(f'INFO: setCurrentOffset({offset:08X})')
        self.rootSelectionStart = offset
        self.rootSelectionEnd = offset+1
        UIContext.updateStatus(True)

    def getFont(self):
        return binaryninjaui.getMonospaceFont(self)

    def navigate(self, addr):
        #print(f'INFO: navigate({addr:08X})')
        self.rootSelectionStart = addr
        self.rootSelectionEnd = addr+1
        self.hexWidget.setSelectionRange(addr, addr+1)
        return True

    def navigateToFileOffset(self, offset):
        #log_debug('navigateToFileOffset()')
        return False

    def onTreeSelect(self, wtf=None):
        # get KaitaiTreeWidgetItem
        items = self.treeWidget.selectedItems()
        if not items or len(items)<1:
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
        self.structPath.setText('root.' + structPath)

        #
        start, end = int(item.text(2), 16), int(item.text(3), 16)
        if start == None or end == None:
            return

        #print(f'INFO: should highlight addresses [0x{start:X}, 0x{end:X})')

        self.rootSelectionStart = start
        self.rootSelectionEnd = end

        self.hexWidget.setSelectionRange(start, end)

        return

        # determine current IO we're in (the Kaitai input/output abstraction)
        _io = None
        # if the tree item is linked to a KaitaiNode, simply read the IO
        if item.ksobj:
            _io = item.ksobj._parent._io
        else:
            # else we're a leaf
            parent = item.parent()
            if parent:
                # a leaf with a parent -> read parent's IO
                _io = parent.ksobj._io
            else:
                # a leaf without a parent -> we must be at root -> use root IO
                _io = self.ioRoot

        # if the selection is in the root view, store the interval so that upon
        # getCurrentOffset() callback, we return the middle and feature map is
        # updated
        if _io == self.ioRoot:
            self.rootSelectionStart = start
            self.rootSelectionEnd = end

        # current kaitai object is on a different io? then swap HexEditor
        if _io != self.ioCurrent:
            # delete old view
            self.hexWidget.hide()
            self.hexWidget.setParent(None)
            self.hexWidget.deleteLater()
            self.hexWidget = None

            # if it's the original file IO, wrap the already-open file binary view
            if _io == self.ioRoot:
                self.hexWidget = HexEditor(self.binaryView, ViewFrame.viewFrameForWidget(self), 0)
            # otherwise delete old view, create a temporary view
            else:
                # create new view
                length = _io.size()
                _io.seek(0)
                data = _io.read_bytes(length)
                bv = binaryview.BinaryView.new(data)
                self.hexWidget = HexEditor(bv, ViewFrame.viewFrameForWidget(self), 0)

            self.splitter.addWidget(self.hexWidget)
            self.ioCurrent = _io

        # now position selection in whatever HexEditor is current
        #log_debug('selecting to [0x%X, 0x%X)' % (start, end))
        self.hexWidget.setSelectionRange(start, end)

        # set hex group title to reflect current selection
        #self.hexGroup.setTitle('Hex View @ [0x%X, 0x%X)' % (start, end))

    def getHeaderOptionsWidget(self):
    #    print('RETURNING THE HEADER OPTIONS WIDGET!')
        return menu.KaitaiOptionsWidget(self)

    #def getStatusBarWidget(self):
    #    print('RETURNING THE STATUS BAR WIDGET!')
    #    return menu.KaitaiStatusBarWidget(self)

class KaitaiViewType(ViewType):
    def __init__(self):
        super(KaitaiViewType, self).__init__("Kaitai", "Kaitai")

    # binaryView:        BinaryView
    def getPriority(self, binaryView, filename):
        #return 100
        #log_debug('len(bv)=0x%X executable=%d bytes=%s' % (len(binaryView), binaryView.executable, repr(binaryView.read(0,4))))

        # executable means the view is mapped like an OS loader would load an executable (eg: view=ELF)
        # !executable means executable image is not mapped (eg: view=Raw) (or something like .png is loaded)
        if binaryView.executable:
            return 0

        if binaryView.start != 0:
            return 1

        dataSample = binaryView.read(0, 16)
        if len(dataSample) != 16:
            return 1

        # if we don't recognize it, return 1
        ksModuleName = kshelpers.infer_kaitai_module(dataSample, binaryView.length, filename)
        if not ksModuleName:
            return 1

        # for executables, yield to triage (25)
        if ksModuleName in ['elf', 'microsoft_pe', 'mach_o']:
            return 24

        #
        return 100

    def create(self, binaryView, view_frame):
        return KaitaiView(view_frame, binaryView)

ViewType.registerViewType(KaitaiViewType())
