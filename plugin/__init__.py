import sys

try:
    from . import view

except Exception as e:
    print('Unable to import view, assuming commandline invocation.')
