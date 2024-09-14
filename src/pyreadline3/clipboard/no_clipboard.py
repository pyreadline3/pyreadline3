# -*- coding: utf-8 -*-
# *****************************************************************************
#       Copyright (C) 2006-2020 Jorgen Stenarson. <jorgen.stenarson@bostream.nu>
#       Copyright (C) 2020 Bassem Girgis. <brgirgis@gmail.com>
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
# *****************************************************************************


_global_clipboard_buffer = ""


def GetClipboardText():
    return _global_clipboard_buffer


def SetClipboardText(text):
    global _global_clipboard_buffer
    _global_clipboard_buffer = text
