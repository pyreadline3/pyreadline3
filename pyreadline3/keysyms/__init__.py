from __future__ import absolute_import, print_function, unicode_literals

import sys

from . import winconstants

in_ironpython = "IronPython" in sys.version

if in_ironpython:
    try:
        from .ironpython_keysyms import *
    except ImportError as x:
        raise ImportError(
            "Could not import keysym for local ironpython version") from x
else:
    try:
        from .keysyms import *
    except ImportError as x:
        raise ImportError(
            "Could not import keysym for local python version") from x
