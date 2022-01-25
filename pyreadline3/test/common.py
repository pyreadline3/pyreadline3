# -*- coding: utf-8 -*-
# *****************************************************************************
#       Copyright (C) 2006-2020  Michael Graz. <mgraz@plan10.com>
#       Copyright (C) 2020 Bassem Girgis. <brgirgis@gmail.com>
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
# *****************************************************************************
from __future__ import absolute_import, print_function, unicode_literals

from pyreadline3 import keysyms
from pyreadline3.lineeditor import history, lineobj


class MockReadline:
    def __init__(self):
        self.l_buffer = lineobj.ReadLineTextBuffer("")
        self._history = history.LineHistory()

    def add_history(self, line):
        self._history.add_history(lineobj.TextLine(line))

    def _print_prompt(self):
        pass

    def _bell(self):
        pass

    def insert_text(self, string):
        '''Insert text into the command line.'''
        self.l_buffer.insert_text(string)


class MockConsole:
    def __init__(self):
        self.bell_count = 0
        self.text = ''

    def size(self):
        return (1, 1)

    def cursor(self, visible=None, size=None):
        pass

    def bell(self):
        self.bell_count += 1

    def write(self, text):
        self.text += text


class Event:
    def __init__(self, char):
        if char == "escape":
            self.char = '\x1b'
        elif char == "backspace":
            self.char = '\x08'
        elif char == "tab":
            self.char = '\t'
        elif char == "space":
            self.char = ' '
        else:
            self.char = char


def keytext_to_keyinfo_and_event(keytext):
    keyinfo = keysyms.common.make_KeyPress_from_keydescr(keytext)
    if len(keytext) == 3 and keytext[0] == '"' and keytext[2] == '"':
        event = Event(keytext[1])
    else:
        event = Event(keyinfo.tuple()[3])
    return keyinfo, event
