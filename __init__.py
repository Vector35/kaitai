import sys

if sys.argv[0:] and sys.argv[0]=='-m':
    pass
else:
    from . import view
