import binaryninja

if binaryninja.core_ui_enabled():
    # MODE: GUI
    from .ui import view
    from binaryninjaui import ViewType
    ViewType.registerViewType(view.KaitaiViewType())
else:
    # MODE: headless
    pass
