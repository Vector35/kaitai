#!/usr/bin/env python

# exercise essential Kaitai Struct functionality on the command line (no Binja UI)

import sys
import kshelpers


def print_tree(node: kshelpers.TreeNode, depth=0):
    indent = '  ' * depth
    print(indent + str(node))
    for child in node.children:
        print_tree(child, depth + 1)


def file_to_tree(path: str) -> kshelpers.TreeNode:
    kt_struct = kshelpers.parse_file_path(path)
    assert kt_struct is not None
    return kshelpers.build_tree(kt_struct)


if __name__ == '__main__':
    file_path = sys.argv[1:]
    if not file_path:
        print("Please provide a file!")
    else:
        print(f'-------- OPENING {file_path[0]} --------')
        tree = file_to_tree(file_path[0])
        print_tree(tree)
        print()
