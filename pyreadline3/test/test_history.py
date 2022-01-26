# -*- coding: UTF-8 -*-
# *****************************************************************************
#       Copyright (C) 2006-2020 Jorgen Stenarson. <jorgen.stenarson@bostream.nu>
#       Copyright (C) 2020 Bassem Girgis. <brgirgis@gmail.com>
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
# *****************************************************************************
from __future__ import absolute_import, print_function, unicode_literals

import sys
import unittest

import pyreadline3.logger
from pyreadline3.lineeditor import lineobj
from pyreadline3.lineeditor.history import LineHistory

sys.path.append('../..')

pyreadline3.logger.sock_silent = False

# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
RL = lineobj.ReadLineTextBuffer


class Test_prev_next_history(unittest.TestCase):
    t = "test text"

    def setUp(self):
        self.q = q = LineHistory()
        for x in ["aaaa", "aaba", "aaca", "akca", "bbb", "ako"]:
            q.add_history(RL(x))

    def test_previous_history(self):
        hist = self.q
        assert hist.history_cursor == 6
        t_line = RL("")
        hist.previous_history(t_line)
        assert t_line.get_line_text() == "ako"
        hist.previous_history(t_line)
        assert t_line.get_line_text() == "bbb"
        hist.previous_history(t_line)
        assert t_line.get_line_text() == "akca"
        hist.previous_history(t_line)
        assert t_line.get_line_text() == "aaca"
        hist.previous_history(t_line)
        assert t_line.get_line_text() == "aaba"
        hist.previous_history(t_line)
        assert t_line.get_line_text() == "aaaa"
        hist.previous_history(t_line)
        assert t_line.get_line_text() == "aaaa"

    def test_next_history(self):
        hist = self.q
        hist.beginning_of_history()
        assert hist.history_cursor == 0
        t_line = RL("")
        hist.next_history(t_line)
        assert t_line.get_line_text() == "aaba"
        hist.next_history(t_line)
        assert t_line.get_line_text() == "aaca"
        hist.next_history(t_line)
        assert t_line.get_line_text() == "akca"
        hist.next_history(t_line)
        assert t_line.get_line_text() == "bbb"
        hist.next_history(t_line)
        assert t_line.get_line_text() == "ako"
        hist.next_history(t_line)
        assert t_line.get_line_text() == "ako"


class Test_prev_next_history1(unittest.TestCase):
    t = "test text"

    def setUp(self):
        self.q = q = LineHistory()
        for x in ["aaaa", "aaba", "aaca", "akca", "bbb", "ako"]:
            q.add_history(RL(x))

    def test_history_search_backward(self):
        q = LineHistory()
        for x in ["aaaa", "aaba", "aaca", "    aacax", "akca", "bbb", "ako"]:
            q.add_history(RL(x))
        a = RL("aa", point=2)
        for x in ["aaca", "aaba", "aaaa", "aaaa"]:
            res = q.history_search_backward(a)
            assert res.get_line_text() == x

    def test_history_search_forward(self):
        q = LineHistory()
        for x in ["aaaa", "aaba", "aaca", "    aacax", "akca", "bbb", "ako"]:
            q.add_history(RL(x))
        q.beginning_of_history()
        a = RL("aa", point=2)
        for x in ["aaba", "aaca", "aaca"]:
            res = q.history_search_forward(a)
            assert res.get_line_text() == x


class Test_history_search_incr_fwd_backwd(unittest.TestCase):
    def setUp(self):
        self.q = q = LineHistory()
        for x in ["aaaa", "aaba", "aaca", "akca", "bbb", "ako"]:
            q.add_history(RL(x))

    def test_backward_1(self):
        q = self.q
        self.assertEqual(q.reverse_search_history("b"), "bbb")
        self.assertEqual(q.reverse_search_history("b"), "aaba")
        self.assertEqual(q.reverse_search_history("bb"), "aaba")

    def test_backward_2(self):
        q = self.q
        self.assertEqual(q.reverse_search_history("a"), "ako")
        self.assertEqual(q.reverse_search_history("aa"), "aaca")
        self.assertEqual(q.reverse_search_history("a"), "aaca")
        self.assertEqual(q.reverse_search_history("ab"), "aaba")

    def test_forward_1(self):
        q = self.q
        self.assertEqual(q.forward_search_history("a"), "ako")

    def test_forward_2(self):
        q = self.q
        q.history_cursor = 0
        self.assertEqual(q.forward_search_history("a"), "aaaa")
        self.assertEqual(q.forward_search_history("a"), "aaba")
        self.assertEqual(q.forward_search_history("ak"), "akca")
        self.assertEqual(q.forward_search_history("akl"), "akca")
        self.assertEqual(q.forward_search_history("ak"), "akca")
        self.assertEqual(q.forward_search_history("ako"), "ako")


class Test_empty_history_search_incr_fwd_backwd(unittest.TestCase):
    def setUp(self):
        self.q = LineHistory()

    def test_backward_1(self):
        q = self.q
        self.assertEqual(q.reverse_search_history("b"), "")

    def test_forward_1(self):
        q = self.q
        self.assertEqual(q.forward_search_history("a"), "")


# ----------------------------------------------------------------------
# utility functions

# ----------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
