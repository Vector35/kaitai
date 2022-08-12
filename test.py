#!/usr/bin/env python

# exercise essential Kaitai Struct functionality on the command line (no Binja UI)

import os, sys

sys.path.append('./corelogic')
import kshelpers

sys.path.append('./formats')

def print_tree(node, depth=0):
    indent = '  '*depth
    print(indent + str(node))
    for child in node.children:
        print_tree(child, depth+1)

def file_to_tree(fpath):
    ksobj = kshelpers.parseFpath(fpath)

    tree = kshelpers.build_tree(ksobj)
    tree.name = 'root'
    tree.start = 0
    tree.end = os.path.getsize(fpath)

    return tree

if __name__ == '__main__':
    fpaths = []

    if sys.argv[1:]:
        fpaths = [sys.argv[1]]
    else:
        fpaths = [os.path.join(os.environ['HOME'], 'fdumps', 'filesamples', fname) for fname in
            [
            # binaries
            'ntdll-aarch64.dll', 'hello-android-aarch64.elf',
            'helloworld_with_condition_aarch64_elf', 'hello-linux-x64.elf',
            'hello-linux-ppc32.elf', 'hello-android-thumb.elf',
            'hello-windows-x86.pe32.exe', 'hello-macos-x64.macho', 'hello_windows_x64.exe',
            'hello-sh4', 'hello.exe', 'hello-linux-ppc64',
            # image formats
            'lena.bmp', 'lena.gif', 'lena.png',
            # archives
            'elephbrain.rar', 'MSPACMAN.zip',
            # misc
            'classes.dex'
            ]]

    for fpath in fpaths:
        print(f'-------- OPENING {fpath} --------')
        tree = file_to_tree(fpath)
        print_tree(tree)
        print()

