#!/usr/bin/env python

import traceback

import io
import os
import re
import sys
import enum
import types
import struct
import inspect
import binascii
import importlib
import collections

import kaitaistruct


#------------------------------------------------------------------------------
# id and parse
#------------------------------------------------------------------------------

# return the name of the kaitai module to service this data
#
# dsample:    str        data sample
# length:    int        total length of data
def idData(dataSample, length):
    result = None
    #print('idData() here with sample: %s' % repr(dataSample))

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
    if dataSample[0:2] == b'PK' and dataSample[2:4] in [b'\x01\x02', b'\x03\x04', b'\x05\x06']:
        result = 'zip'
    if dataSample[0:6] == b'Rar!\x1a\x07':
        result = 'rar'
    if dataSample[0:2] == b'\x1f\x8b' and dataSample[2:3]==b'\x08':
        result = 'gzip'

    #print('idData() returning \'%s\'' % result)
    return result

def idFile(fpath):
    with open(fpath, 'rb') as fp:
        return idData(fp.read(16), os.path.getsize(fpath))

def ksModuleToClass(moduleName):
    # split on underscores, camelcase
    return ''.join(map(lambda x: x.capitalize(), moduleName.split('_')))

formats_in_python_path = False
def ksImportClass(moduleName):
    print(f'ksImportClass({moduleName})')

    # add the compiled Kaitai formats to the Python path
    global formats_in_python_path
    if not formats_in_python_path:
        this_file = inspect.stack()[0][1]
        this_dir = os.path.dirname(this_file)
        formats_dir = os.path.join(this_dir, '../formats')
        print(f'Adding {formats_dir} to the python path.') 
        sys.path.append(formats_dir)
        formats_in_python_path = True

    if not moduleName:
        print(f'WARNING: ksImportClass given module name: {moduleName}')
        return None

    classRef = None
    try:
        print(f'INFO: importlib.import_module({moduleName})')
        module = importlib.import_module(moduleName)
        className = ksModuleToClass(moduleName)
        #print('className: -%s-' % className)
        classRef = getattr(module, className)
    except AttributeError as e:
        print('ERROR: importing kaitai module %s' % moduleName)
        pass

    return classRef

def parseFpath(fpath, ksModuleName=None):
    print(f'parseFpath({fpath}, {ksModuleName})')

    if not ksModuleName:
        ksModuleName = idFile(fpath)
    #print('parseFpath() using kaitai format: %s' % ksModuleName)

    ksClass = ksImportClass(ksModuleName)
    if not ksClass:
        print(f'ERROR: importing {ksModuleName} to service {fpath}')
        return None

    parsed = None
    #try:
    parsed = ksClass.from_file(fpath)
    parsed._read()
    exercise_re(parsed)
    #except Exception as e:
    #    print('parseFpath(): kaitai module %s threw exception, check file type' % ksModuleName)
    #    parsed = None

    return parsed

def parseData(data, ksModuleName=None):
    print(f'parseData(data, {ksModuleName})')

    if not ksModuleName:
        ksModuleName = idData(data, len(data))
    #print('parseData() using kaitai format: %s' % ksModuleName)

    ksClass = ksImportClass(ksModuleName)
    if not ksClass:
        print(f'ERROR: importing {ksModuleName} to service {fpath}')
        return None

    parsed = None
    try:
        parsed = ksClass.from_bytes(data)
        parsed._read()
        exercise_re(parsed)
    except Exception as e:
        print('parseData(): kaitai module %s threw exception, check file type' % ksModuleName)
        parsed = None

    return parsed

def parseIo(ioObj, ksModuleName=None):
    print(f'parseIo(ioObj, {ksModuleName})')

    ioObj.seek(0, io.SEEK_END)
    length = ioObj.tell()

    if not ksModuleName:
        ioObj.seek(0, io.SEEK_SET)
        ksModuleName = idData(ioObj.read(16), length)
    #print('parseIo() using kaitai format: %s' % ksModuleName)

    ioObj.seek(0, io.SEEK_SET)
    ksClass = ksImportClass(ksModuleName)
    if not ksClass: return None

    parsed = None
    try:
        ioObj.seek(0, io.SEEK_SET)
        parsed = ksClass.from_io(ioObj)
        parsed._read()
        exercise_re(parsed)
    except Exception as e:
        print('parseIo(): kaitai module %s threw exception %s, check file type' % (ksModuleName, str(e)))
        parsed = None

    return parsed

#------------------------------------------------------------------------------
# misc
#------------------------------------------------------------------------------

def objToStr(obj):
    objType = type(obj)

    # blacklist: functions, types, callables
    #
    if isinstance(obj, type):
        #print('reject %s because its a type' % field_name)
        return '(type)'
    elif hasattr(obj, '__call__'):
        #print('reject %s because its a callable' % field_name)
        return '(callable)'

    result = None

    # whitelist: strings, unicodes, bytes, ints, bools, enums
    #
    if obj == None:
        return 'None'
    elif isinstance(obj, str):
        if len(obj) > 8:
            result = '%s...%s (0x%X==%d chars total)' % \
                (repr(obj[0:8]), repr(obj[-1]), len(obj), len(obj))
        else:
            result = repr(obj)
    elif isinstance(obj, bytes):
        if len(obj) > 8:
            result = binascii.hexlify(obj[0:8]).decode('utf-8') + '...' + \
                ('%02X' % obj[-1]) + ' (0x%X==%d bytes total)' % (len(obj), len(obj))
        else:
            result = binascii.hexlify(obj).decode('utf-8')
    # note: bool needs to appear before int (else int determination will dominate)
    elif isinstance(obj, bool):
        result = '%s' % (obj)
    elif isinstance(obj, int):
        result = '0x%X (%d)' % (obj, obj)
    elif str(objType).startswith('<enum '):
        result = '%s' % (obj)
    elif isinstance(obj, list):
        result = repr(obj)
    elif isinstance(obj, kaitaistruct.KaitaiStruct):
        return re.match(r'^.*\.(\w+) object at ', repr(obj)).group(1)
    elif isinstance(obj, kaitaistruct.KaitaiStream):
        return re.match(r'^.*\.(\w+) object at ', repr(obj)).group(1)
    elif isinstance(obj, collections.defaultdict):
        # probably _debug
        result = repr(obj)
    else:
        result = '(unknown type %s)' % (str(objType))

    return result

# access all fields that may be properties, which could compute internal results
# (often '_m_XXX' fields)
#
# mark "exercised" kaitai structs with the _exercised attribute
def exercise_re(ksobj):
    queue = []

    for aname in dir(ksobj):
        try:
            attr = getattr(ksobj, aname, False)
            if isinstance(attr, kaitaistruct.KaitaiStruct) and not getattr(attr, '_exercised', False):
                setattr(attr, '_exercised', True)
                queue.append(attr)
        except AttributeError:
            pass

    #print('recursion queue: ' + str(queue))
    for attr in queue:
        exercise_re(attr)

#------------------------------------------------------------------------------
# kaitai object exploring stuff
#------------------------------------------------------------------------------

# return all field names qualified for printing
#
def getfield_namesPrint(ksobj):
    result = []

    for field_name in dir(ksobj):
        if isFieldExceptionPrint(field_name):
            continue

        try:
            subobj = getattr(ksobj, field_name, False)

            # do not return kaitai objects (are for descending, not printing)
            if isinstance(subobj, kaitaistruct.KaitaiStruct):
                continue
            elif isinstance(subobj, list):
                if len(subobj)<=0 or isinstance(subobj[0], kaitaistruct.KaitaiStruct):
                    continue

            #print('%s is ok' % field_name)
            #print('%s is instance? %s' % (field_name, isinstance(subobj, kaitaistruct.KaitaiStruct)))
            result.append(field_name)
        except AttributeError:
            pass

    return result

# return all field names required for descending
#
# IN:    kaitai object
# OUT:    field names that are either:
#        - kaitai objects
#        - lists of kaitai objects
#
def getfield_namesDescend(ksobj):
    result = []

    for field_name in dir(ksobj):
        if isFieldExceptionDescend(field_name):
            continue

        try:
            subobj = getattr(ksobj, field_name, False)

            if isinstance(subobj, kaitaistruct.KaitaiStruct):
                result += [field_name]
            elif isinstance(subobj, list):
                if len(subobj)>0 and isinstance(subobj[0], kaitaistruct.KaitaiStruct):
                    result += [field_name]
        except AttributeError:
            pass

    return result

# compute all kaitai objects linked to from the given object
#
# IN:    kaitai object
# OUT:    [obj0, obj1, obj2, ...]
#
def getLinkedKaitaiObjects(ksobj):
    result = set()

    for field_name in getfield_namesDescend(ksobj):
        subobj = getattr(ksobj, field_name, False)
        if isinstance(subobj, list):
            for tmp in subobj:
                result.add(tmp)
        else:
            result.add(subobj)

    return result

# compute all kaitai objects linked to from the given object, and from its
# descendents, and so on...
def getLinkedKaitaiObjectsAll(ksobj, depth=0):
    #if depth > 2:
    #    return []
    result = set([ksobj])

    linkedObjects = getLinkedKaitaiObjects(ksobj)
    for subobj in linkedObjects:
        subResult = getLinkedKaitaiObjectsAll(subobj, depth+1)
        result = result.union(subResult)

    return result

def getDepth(ksobj, depth=0):
    result = depth

    for subObj in getLinkedKaitaiObjects(ksobj):
        result = max(result, getDepth(subObj, depth+1))

    return result

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
# - centralized location to modify field names and labels (eg: remove '_m_')

class TreeNode():
    def __init__(self, name=None):

        self.name = name    # string
        
        self.start = None    # int
        self.end = None        # int

        self.value = None    # string

        self.ksobj = None    # KaitaiStruct
        self.children = []

    def __str__(self):
        result = ''

        if self.start != None and self.end != None:
            result += f' [{self.start:08X},{self.end:08X})'
        else:
            result += f' [{self.start}, {self.end})'

        result += ' '+self.name

        if self.value:
            result += f' value=\'{self.value}\''

        if self.ksobj:
            result += ' ksobj=%s' % self.ksobj
            result += ' io=%s' % self.ksobj._io

        return result

#------------------------------------------------------------------------------
# build QTree and helpers
#------------------------------------------------------------------------------

def build_tree(ksobj):
    assert isinstance(ksobj, kaitaistruct.KaitaiStruct)

    node = TreeNode()

    field_names = list(ksobj._debug.keys())
    field_names = [x[3:] if x.startswith('_m_') else x for x in field_names]
    for field_name in field_names:
        attr = getattr(ksobj, field_name)

        # CASE0: attribute is a KaitaiStruct
        if isinstance(attr, kaitaistruct.KaitaiStruct):
            child = build_tree(attr)
            populate_child(ksobj, field_name, None, child)
            node.children.append(child)

        # CASE1: attribute is a list
        elif isinstance(attr, list):
            child = TreeNode()
            populate_child(ksobj, field_name, None, child)
            node.children.append(child)

            # CASE1.0: list of KaitaiObjects
            if isinstance(attr[0], kaitaistruct.KaitaiStruct):
                for i in range(len(attr)):
                    gc_name = f'{field_name}[{i}]'
                    grandchild = build_tree(attr[i])
                    populate_child(ksobj, gc_name, None, grandchild)
                    child.children.append(grandchild)

            # CASE1.1: list of primitives
            else:
                for i in range(len(attr)):
                    gc_name = f'{field_name}[{i}]'
                    grandchild = create_leaf(gc_name, attr[i])
                    populate_child(ksobj, gc_name, None, grandchild)
                    child.children.append(grandchild)

        # CASE2: attribute is primitive
        else:
            child = create_leaf(field_name, attr)
            populate_child(ksobj, field_name, None, child)
            node.children.append(child)

    return node

def create_leaf(field_name, obj):
    objtype = type(obj)

    if objtype == types.FunctionType:
        #print('reject %s because its a function' % field_name)
        return None
    elif isinstance(obj, type):
        #print('reject %s because its a type' % field_name)
        return None
    elif hasattr(obj, '__call__'):
        #print('reject %s because its a callable' % field_name)
        return None

    field_value = None

    if isinstance(obj, str) or isinstance(obj, bytes):
        if len(obj) > 8:
            field_value = str(repr(obj[0:8])) + '...'
        else:
            field_value = repr(obj)
    elif isinstance(obj, int):
        field_value = '0x%X (%d)' % (obj, obj)
    elif isinstance(obj, bool):
        field_value = '%s' % (obj)
    elif str(objtype).startswith('<enum '):
        field_value = '%s' % (obj)
    else:
        #print('field %s has type: -%s-' % (field_name,str(objtype)))
        pass

    if field_value:
        node = TreeNode()
        node.name = field_name
        node.value = field_value
        return node
    else:
        #print('rejected leaf node to %s' % field_name)
        #print(obj)
        #print(type(obj))
        return None

# ARG                TYPE                    NOTES
# --------           -------                 -------
# ksobj:             KaitaiStruct            the current one we're on
# field_name:        string                  actual field name inside the kaitai struct
# field_value:       string                  value used in the tree view
# node:              TreeNode                the item to which we want to imprint(start/end)
def populate_child(ksobj, field_name, field_value, node):
    node.name = field_name

    if field_value:
        node.value = field_value

    # name like "foo[5]"
    if m := re.match(r'(.*)\[(\d+)\]', field_name):
        fnbase = m.group(1)
        fnidx = int(m.group(2))
        arr_info = ksobj._debug[fnbase].get('arr', None) or \
                   ksobj._debug['_m_'+fnbase].get('arr', None)
        start, end = arr_info[fnidx]['start'], arr_info[fnidx]['end']
    # name like "foo"
    else:
        start = ksobj._debug[field_name].get('start', None)
        if start == None:
            start = ksobj._debug['_m_'+field_name].get('start', None)

        end = ksobj._debug[field_name].get('end', None)
        if end == None:
            end = ksobj._debug['_m_'+field_name].get('end', None)

    if start != None:
        node.start = start
    if end != None:
        node.end = end

