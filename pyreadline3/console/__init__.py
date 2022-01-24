from __future__ import absolute_import, print_function, unicode_literals

import sys

in_ironpython = "IronPython" in sys.version

if in_ironpython:
    try:
        from .ironpython_console import *
    except ImportError as x:
        raise ImportError(
            "Could not find a console implementation for local "
            "ironpython version") from x
else:
    try:
        from .console import *
    except ImportError as x:
        raise ImportError(
            "Could not find a console implementation for local "
            "python version") from x
