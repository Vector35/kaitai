import binaryninja

if binaryninja.core_ui_enabled():
    # MODE: GUI

    # get the corelogic in syspath so plugin will be able to import kshelpers, kaitaistruct modules
    import os
    import sys
    import inspect
    this_file = inspect.stack()[0][1]
    this_dir = os.path.dirname(this_file)
    this_dir = os.path.realpath(this_dir)
    cl_dir = os.path.join(this_dir, '..', 'corelogic')
    sys.path.append(cl_dir)

    # import the UI
    from . import view
else:
    # MODE: headless
    pass
