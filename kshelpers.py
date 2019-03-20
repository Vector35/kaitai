#!/usr/bin/env python

import io
import os
import sys
import struct
import types
import importlib

import binaryninja

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QTreeWidgetItem

if sys.version_info[0] == 2:
	import kaitaistruct
else:
	from . import kaitaistruct

#------------------------------------------------------------------------------
# id and parse
#------------------------------------------------------------------------------

# return the name of the kaitai module to service this data
#
# dsample:	str		data sample
# length:	int		total length of data
def idData(dataSample, length):
	result = None

	if len(dataSample) < 16:
		return result

	if dataSample[0:4] == b'\x7fELF':
		result = 'elf'
	if dataSample[0:4] in [b'\xfe\xed\xfa\xce', b'\xce\xfa\xed\xfe', b'\xfe\xed\xfa\xcf', b'\xcf\xfa\xed\xfe']:
		result = 'mach_o'
	if dataSample[0:2] == b'MZ':
		result = 'microsoft_pe'
	if dataSample[0:8] == b'\x89PNG\x0d\x0a\x1a\x0a':
		result = 'png'
	if dataSample[2:11] == b'\xFF\xe0\x00\x10JFIF\x00':
		result = 'jpeg'
	if dataSample[0:4] == b'GIF8':
		result = 'gif'
	if dataSample[0:2] in [b'BM', b'BA', b'CI', b'CP', b'IC', b'PT'] and struct.unpack('<I', dataSample[2:6])[0]==length:
		result = 'bmp'

	#print('ioData() returning \'%s\'' % result)
	return result

def idFile(fpath):
	with open(fpath, 'rb') as fp:
		return idData(fp.read(16), os.path.getsize(fpath))

def ksModuleToClass(moduleName):
	# split on underscores, camelcase
	return ''.join(map(lambda x: x.capitalize(), moduleName.split('_')))

def ksImportClass(moduleName):
	global __name__, __package__
	if not moduleName:
		return None
	
	classThing = None
	try:
		#print('__package__: -%s-' % __package__)	# 'kaitai'
		#print('__name__: -%s-' % __name__)			# 'kaitai.kshelpers'

		#print('moduleName: -%s-' % moduleName)
		module = importlib.import_module('.'+moduleName, __package__)
		className = ksModuleToClass(moduleName)
		#print('className: -%s-' % className)
		classThing = getattr(module, className)
	except Exception as e:
		print(e)
		pass

	return classThing

def parseFpath(fpath):
	ksClass = ksImportClass(idFile(fpath))
	if not ksClass: return None

	parsed = ksClass.from_file(fpath)
	parsed._read()
	return parsed

def parseData(data):
	ksClass = ksImportClass(idData(data), len(data))
	if not ksClass: return None

	parsed = ksClass.from_bytes(data)
	parsed._read()
	return parsed

def parseIo(ioObj):
	ioObj.seek(0, io.SEEK_END)
	length = ioObj.tell()

	ioObj.seek(0, io.SEEK_SET)
	ksClass = ksImportClass(idData(ioObj.read(16), length))
	if not ksClass: return None

	ioObj.seek(0, io.SEEK_SET)
	parsed = ksClass.from_io(ioObj)
	parsed._read()
	return parsed

#------------------------------------------------------------------------------
# Kaitai IO Wrapper
#------------------------------------------------------------------------------

# wraps a BinaryView into an "IO" that KaitaiStream can use
#
# now Kaitai can parse directly from the BinaryView and we can avoid making a
# potentially giant copy of the file contents just for kaitai parsing
#
class KaitaiBinaryViewIO:
	def __init__(self, binaryView):
		self.binaryView = binaryView
		self.position = 0

	def seek(self, offs, whence=io.SEEK_SET):
		#print('seek(0x%X, %d)' % (offs, whence))
		if whence == io.SEEK_SET:
			self.position = offs
		elif whence == io.SEEK_CUR:
			self.position += offs
		elif whence == io.SEEK_END:
			self.position = len(self.binaryView)
		else:
			raise Exception('unknown whence in seek(): %d' % whence)

	def tell(self):
		#print('tell() returning 0x%X' % (self.position))
		return self.position

	def read(self, length=None):
		# if no length is given (eg: see read_bytes_full() in kaitaistruct.py)
		if length == None:
			length = len(self.binaryView) - self.position

		#print('read(%d) (starting at position: 0x%X)' % (length, self.position))
		data = self.binaryView.read(self.position, length)
		self.position += length
		return data

	def close(self):
		pass

#------------------------------------------------------------------------------
# Qt/Kaitai OOP
#------------------------------------------------------------------------------

# why subclass?
# - override "<" to get sorting to work right
# - setLabel(), setValue(), etc. conveniences
# - centralized location to modify field names and labels (eg: remove '_m_')

class KaitaiTreeWidgetItem(QTreeWidgetItem):
	def __init__(self, parent=None, data=[None,None,None,None]):
		QTreeWidgetItem.__init__(self, parent, data)

		self.label = None	# string
		self.value = None	# string
		self.start = None	# int
		self.end = None		# int
		self.ksobj = None	# KaitaiStruct

	def __lt__(self, otherItem):
		column = self.treeWidget().sortColumn()

		lhsText = self.text(column)
		rhsText = otherItem.text(column)

		if not lhsText:
			return False
		if not rhsText:
			return True

		try:
			return int(lhsText,16) < int(rhsText, 16)
		except:
			return lhsText.__lt__(rhsText)

	def setLabel(self, label):
		self.label = label
		if label.startswith('_m_'):
			label = label[3:]
		self.setData(0, Qt.DisplayRole, label)

	def setValue(self, value):
		self.value = value
		if isinstance(value, int):
			value = '%X'%value
		self.setData(1, Qt.DisplayRole, value)

	def setStart(self, start):
		if start == None:
			self.start = None
		elif isinstance(start, int):
			self.start = start
			start = '%X'%start
		elif (sys.version_info[0] == 2) and type(start) == types.LongType:
			self.start = start
			start = '%X'%start
		else:
			self.start = int(start,16)

		self.setData(2, Qt.DisplayRole, start)

	def setEnd(self, end):
		if end == None:
			self.end = None

		if isinstance(end, int):
			self.end = end
			end = '%X'%end
		elif (sys.version_info[0] == 2) and type(end) == types.LongType:
			self.end = end
			end = '%X'%end
		else:
			self.end = int(end,16)
		self.setData(3, Qt.DisplayRole, end)

	def setKaitaiObject(self, ksobj):
		self.ksobj = ksobj
		self.setData(0, Qt.UserRole, ksobj)

	def __str__(self):
		result = 'label=%s: value=%s range=[%s,%s)' % \
			(self.label, self.value, self.start, self.end)

		result += ' ksobj=%s' % self.ksobj

		if self.ksobj:
			result += ' io=%s' % self.ksobj._io

		#if self.parent:
		#	result += ' parent=%s' % self.ksobj.parent

		return result

	def __str_short__(self):
		return '[%s,%s) %s' % (repr(self.start), repr(self.end), repr(self.label))

#------------------------------------------------------------------------------
# build QTree and helpers
#------------------------------------------------------------------------------

# ARGS:
# obj:		KaitaiStruct
# RETURNS:
# KaitaiTreeWidgetItem (QTreeWidgetItem)
#
def buildQtree(ksobj):
	if not isinstance(ksobj, kaitaistruct.KaitaiStruct):
		return None

	exceptions = ['_root', '_parent', '_io', 'SEQ_FIELDS', '_debug']

	qwi = KaitaiTreeWidgetItem()
	qwi.setKaitaiObject(ksobj)

	for fieldName in dir(ksobj):
		if hasattr(ksobj, fieldName):
			getattr(ksobj, fieldName)

	fields = dir(ksobj)
	for fieldName in fields:
		if fieldName.startswith('_') and (not fieldName.startswith('_m_')):
			continue
		if fieldName in exceptions:
			continue
		if not hasattr(ksobj, fieldName):
			continue
		if ('_m_'+fieldName) in fields:
			# favor the '_m_' version which seems to get the debug info
			continue
		
		subObj = getattr(ksobj, fieldName)

		child = None
		if isinstance(subObj, kaitaistruct.KaitaiStruct):
			fieldLabel = fieldName
			child = buildQtree(subObj)
			if child:
				populateChild(ksobj, fieldName, fieldName, None, child)
			qwi.addChild(child)

		elif isinstance(subObj, list):
			if len(subObj)<=0:
				continue

			# CASE: is list of KaitaiObjects -> recurse!
			if isinstance(subObj[0], kaitaistruct.KaitaiStruct):
				child = KaitaiTreeWidgetItem()
				populateChild(ksobj, fieldName, fieldName, None, child)

				# does _debug have an array version of start/end?
				startsEnds = None
				if hasattr(ksobj, '_debug'):
					if fieldName in ksobj._debug:
						if 'arr' in ksobj._debug[fieldName]:
							startsEnds = ksobj._debug[fieldName]['arr']

				for i in range(len(subObj)):
					grandchild = buildQtree(subObj[i])
					fieldLabel = '%s[%d]' % (fieldName, i)
					grandchild.setLabel(fieldLabel)

					if startsEnds:
						grandchild.setStart(startsEnds[i]['start'])
						grandchild.setEnd(startsEnds[i]['end'])

					child.addChild(grandchild)

				qwi.addChild(child)

			# CASE: is list of primitive objects -> create leaves
			else:
				child = KaitaiTreeWidgetItem()
				populateChild(ksobj, fieldName, fieldName, None, child)

				# TODO: explain this hack
				kstmp = kaitaistruct.KaitaiStruct(ksobj._io)
				kstmp._parent = ksobj
				child.setKaitaiObject(kstmp)

				# does _debug have an array version of start/end?
				startsEnds = None
				if hasattr(ksobj, '_debug'):
					if fieldName in ksobj._debug:
						if 'arr' in ksobj._debug[fieldName]:
							startsEnds = ksobj._debug[fieldName]['arr']

				for i in range(len(subObj)):
					grandchild = createLeaf('%s[%d]'%(fieldName,i), subObj[i])
					if not grandchild:
						continue

					if startsEnds:
						grandchild.setStart(startsEnds[i]['start'])
						grandchild.setEnd(startsEnds[i]['end'])

					child.addChild(grandchild)

				qwi.addChild(child)
		else:
			child = createLeaf(fieldName, subObj)
			if child:
				# don't override createLeaf()'s work on label, value
				populateChild(ksobj, fieldName, None, None, child)
				qwi.addChild(child)

	return qwi

def createLeaf(fieldName, obj):
	objtype = type(obj)

	if objtype == types.FunctionType:
		#print('reject %s because its a function' % fieldName)
		return None
	elif isinstance(obj, type):
		#print('reject %s because its a type' % fieldName)
		return None
	elif sys.version_info[0] == 2 and callable(obj):
		#print('reject %s because its a callable' % fieldName)
		return None
	elif sys.version_info[0] == 3 and hasattr(obj, '__call__'):
		#print('reject %s because its a callable' % fieldName)
		return None

	fieldValue = None

	if isinstance(obj, str):
		fieldValue = repr(obj)
	elif isinstance(obj, bytes):
		fieldValue = repr(obj)
	elif sys.version_info[0] == 2 and objtype == types.UnicodeType:
		fieldValue = repr(obj)
	elif isinstance(obj, int):
		fieldValue = '0x%X (%d)' % (obj, obj)
	elif isinstance(obj, bool):
		fieldValue = '%s' % (obj)
	elif str(objtype).startswith('<enum '):
		fieldValue = '%s' % (obj)
	else:
		#print('field %s has type: -%s-' % (fieldName,str(objtype)))
		pass

	if fieldValue:
		widget = KaitaiTreeWidgetItem()
		widget.setLabel(fieldName)
		widget.setValue(fieldValue)
		return widget
	else:
		print('rejected leaf node to %s' % fieldName)
		print(obj)
		print(type(obj))
		return None

# ARG				TYPE					NOTES
# ksobj:			KaitaiStruct			the current one we're on
# fieldName:		string					actual field name inside the kaitai struct
# fieldLabel:		string					label used in the tree view
# fieldValue:		string					value used in the tree view
# widget:			KaitaiTreeWidgetItem	the item to which we want to imprint(start/end)
def populateChild(ksobj, fieldName, fieldLabel, fieldValue, widget):
	if fieldLabel:
		widget.setLabel(fieldLabel)
		#print('setting Label: %s' % fieldLabel)
	if fieldValue:
		widget.setValue(fieldValue)

	if (not ksobj) or (not hasattr(ksobj, '_debug')):
		return

	start = None
	if 'start' in ksobj._debug[fieldName]:
		start = ksobj._debug[fieldName]['start']

	end = None
	if 'end' in ksobj._debug[fieldName]:
		end = ksobj._debug[fieldName]['end']

	if start != None:
		widget.setStart(start)
	if end != None:
		widget.setEnd(end)

