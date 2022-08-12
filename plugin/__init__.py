import os
import sys
import inspect

this_file = inspect.stack()[0][1]
this_dir = os.path.dirname(this_file)
this_dir = os.path.realpath(this_dir)
cl_dir = os.path.join(this_dir, '..', 'corelogic')
sys.path.append(cl_dir)

try:
    from . import view

except Exception as e:
    print(e)
    print('Unable to import view, assuming commandline invocation.')
