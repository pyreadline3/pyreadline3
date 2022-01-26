# Copyright (C) 2006  Michael Graz. <mgraz@plan10.com>
from __future__ import absolute_import, print_function, unicode_literals

import sys
import unittest

from pyreadline3.lineeditor import lineobj

sys.path.append('../..')

# ----------------------------------------------------------------------


# ----------------------------------------------------------------------

class Test_copy (unittest.TestCase):
    def test_copy1(self):
        t_line = lineobj.ReadLineTextBuffer("first second")
        q = t_line.copy()
        self.assertEqual(q.get_line_text(), t_line.get_line_text())
        self.assertEqual(q.point, t_line.point)
        self.assertEqual(q.mark, t_line.mark)

    def test_copy2(self):
        t_line = lineobj.ReadLineTextBuffer("first second", point=5)
        q = t_line.copy()
        self.assertEqual(q.get_line_text(), t_line.get_line_text())
        self.assertEqual(q.point, t_line.point)
        self.assertEqual(q.mark, t_line.mark)


class Test_linepos (unittest.TestCase):
    t = "test text"

    def test_NextChar(self):
        t = self.t
        t_line = lineobj.ReadLineTextBuffer(t)
        for i in range(len(t)):
            self.assertEqual(i, t_line.point)
            t_line.point = lineobj.NextChar
        # advance past end of buffer
        t_line.point = lineobj.NextChar
        self.assertEqual(len(t), t_line.point)

    def test_PrevChar(self):
        t = self.t
        t_line = lineobj.ReadLineTextBuffer(t, point=len(t))
        for i in range(len(t)):
            self.assertEqual(len(t) - i, t_line.point)
            t_line.point = lineobj.PrevChar
        # advance past beginning of buffer
        t_line.point = lineobj.PrevChar
        self.assertEqual(0, t_line.point)

    def test_EndOfLine(self):
        t = self.t
        t_line = lineobj.ReadLineTextBuffer(t, point=len(t))
        for i in range(len(t)):
            t_line.point = i
            t_line.point = lineobj.EndOfLine
            self.assertEqual(len(t), t_line.point)

    def test_StartOfLine(self):
        t = self.t
        t_line = lineobj.ReadLineTextBuffer(t, point=len(t))
        for i in range(len(t)):
            t_line.point = i
            t_line.point = lineobj.StartOfLine
            self.assertEqual(0, t_line.point)


class Tests_linepos2(Test_linepos):
    t = "kajkj"


class Tests_linepos3(Test_linepos):
    t = ""


class Test_movement (unittest.TestCase):
    def test_NextChar(self):
        cmd = lineobj.NextChar
        tests = [
            # "First"
            (cmd,
             "First",
             "#     ",
             " #    "),
            (cmd,
                "First",
                "    # ",
                "     #"),
            (cmd,
                "First",
                "     #",
                "     #"),
        ]
        for cmd, text, init_point, expected_point in tests:
            t_line = lineobj.ReadLineTextBuffer(text, get_point_pos(init_point))
            t_line.point = cmd
            self.assertEqual(get_point_pos(expected_point), t_line.point)

    def test_PrevChar(self):
        cmd = lineobj.PrevChar
        tests = [
            # "First"
            (cmd,
             "First",
             "     #",
             "    # "),
            (cmd,
                "First",
                " #   ",
                "#    "),
            (cmd,
                "First",
                "#     ",
                "#     "),
        ]
        for cmd, text, init_point, expected_point in tests:
            t_line = lineobj.ReadLineTextBuffer(text, get_point_pos(init_point))
            t_line.point = cmd
            self.assertEqual(get_point_pos(expected_point), t_line.point)

    def test_PrevWordStart(self):
        cmd = lineobj.PrevWordStart
        tests = [
            # "First Second Third"
            (cmd,
             "First Second Third",
             "                  #",
             "             #     "),
            (cmd,
                "First Second Third",
                "             #     ",
                "      #            "),
            (cmd,
                "First Second Third",
                "     #             ",
                "#                  "),
            (cmd,
                "First Second Third",
                "#                  ",
                "#                  "),
        ]
        for cmd, text, init_point, expected_point in tests:
            t_line = lineobj.ReadLineTextBuffer(text, get_point_pos(init_point))
            t_line.point = cmd
            self.assertEqual(get_point_pos(expected_point), t_line.point)

    def test_NextWordStart(self):
        cmd = lineobj.NextWordStart
        tests = [
            # "First Second Third"
            (cmd,
             "First Second Third",
             "#                 ",
             "      #           "),
            (cmd,
                "First Second Third",
                "    #             ",
                "      #           "),
            (cmd,
                "First Second Third",
                "      #            ",
                "             #     "),
            (cmd,
                "First Second Third",
                "              #    ",
                "                  #"),
        ]
        for cmd, text, init_point, expected_point in tests:
            t_line = lineobj.ReadLineTextBuffer(text, get_point_pos(init_point))
            t_line.point = cmd
            self.assertEqual(get_point_pos(expected_point), t_line.point)

    def test_NextWordEnd(self):
        cmd = lineobj.NextWordEnd
        tests = [
            # "First Second Third"
            (cmd,
             "First Second Third",
             "#                 ",
             "     #            "),
            (cmd,
                "First Second Third",
                "    #             ",
                "     #            "),
            (cmd,
                "First Second Third",
                "      #            ",
                "            #      "),
            (cmd,
                "First Second Third",
                "              #    ",
                "                  #"),
        ]
        for cmd, text, init_point, expected_point in tests:
            t_line = lineobj.ReadLineTextBuffer(text, get_point_pos(init_point))
            t_line.point = cmd
            self.assertEqual(get_point_pos(expected_point), t_line.point)

    def test_PrevWordEnd(self):
        cmd = lineobj.PrevWordEnd
        tests = [
            # "First Second Third"
            (cmd,
             "First Second Third",
             "                  #",
             "            #      "),
            (cmd,
                "First Second Third",
                "            #      ",
                "     #             "),
            (cmd,
                "First Second Third",
                "     #             ",
                "#                  "),
            (cmd,
                "First Second Third",
                "#                  ",
                "#                  "),
        ]
        for cmd, text, init_point, expected_point in tests:
            t_line = lineobj.ReadLineTextBuffer(text, get_point_pos(init_point))
            t_line.point = cmd
            self.assertEqual(get_point_pos(expected_point), t_line.point)

    def test_WordEnd_1(self):
        cmd = lineobj.WordEnd
        tests = [
            # "First Second Third"
            (cmd,
             "First Second Third",
             "#                  ",
             "     #             "),
            (cmd,
                "First Second Third",
                " #                 ",
                "     #             "),
            (cmd,
                "First Second Third",
                "             #     ",
                "                  #"),
        ]
        for cmd, text, init_point, expected_point in tests:
            t_line = lineobj.ReadLineTextBuffer(text, get_point_pos(init_point))
            t_line.point = cmd
            self.assertEqual(get_point_pos(expected_point), t_line.point)

    def test_WordEnd_2(self):
        cmd = lineobj.WordEnd
        tests = [
            # "First Second Third"
            (cmd,
             "First Second Third",
             "     #             "),
            (cmd,
                "First Second Third",
                "            #      "),
            (cmd,
                "First Second Third",
                "                  #"),
        ]

        for cmd, text, init_point in tests:
            t_line = lineobj.ReadLineTextBuffer(text, get_point_pos(init_point))
            self.assertRaises(lineobj.NotAWordError, cmd, t_line)

    def test_WordStart_1(self):
        cmd = lineobj.WordStart
        tests = [
            # "First Second Third"
            (cmd,
             "First Second Third",
             "#                  ",
             "#                  "),
            (cmd,
                "First Second Third",
                " #                 ",
                "#                  "),
            (cmd,
                "First Second Third",
                "               #   ",
                "             #     "),
        ]
        for cmd, text, init_point, expected_point in tests:
            t_line = lineobj.ReadLineTextBuffer(text, get_point_pos(init_point))
            t_line.point = cmd
            self.assertEqual(get_point_pos(expected_point), t_line.point)

    def test_WordStart_2(self):
        cmd = lineobj.WordStart
        tests = [
            # "First Second Third"
            (cmd,
             "First Second Third",
             "     #             "),
            (cmd,
                "First Second Third",
                "            #      "),
            (cmd,
                "First Second Third",
                "                  #"),
        ]

        for cmd, text, init_point in tests:
            t_line = lineobj.ReadLineTextBuffer(text, get_point_pos(init_point))
            self.assertRaises(lineobj.NotAWordError, cmd, t_line)

    def test_StartOfLine(self):
        cmd = lineobj.StartOfLine
        tests = [
            # "First Second Third"
            (cmd,
             "First Second Third",
             "#                 ",
             "#                 "),
            (cmd,
                "First Second Third",
                "         #         ",
                "#                  "),
            (cmd,
                "First Second Third",
                "                  #",
                "#                  "),
        ]
        for cmd, text, init_point, expected_point in tests:
            t_line = lineobj.ReadLineTextBuffer(text, get_point_pos(init_point))
            t_line.point = cmd
            self.assertEqual(get_point_pos(expected_point), t_line.point)

    def test_EndOfLine(self):
        cmd = lineobj.EndOfLine
        tests = [
            # "First Second Third"
            (cmd,
             "First Second Third",
             "#                 ",
             "                  #"),
            (cmd,
                "First Second Third",
                "         #         ",
                "                  #"),
            (cmd,
                "First Second Third",
                "                  #",
                "                  #"),
        ]
        for cmd, text, init_point, expected_point in tests:
            t_line = lineobj.ReadLineTextBuffer(text, get_point_pos(init_point))
            t_line.point = cmd
            self.assertEqual(get_point_pos(expected_point), t_line.point)

    def test_Point(self):
        cmd = lineobj.Point
        tests = [
            # "First Second Third"
            (cmd,
             "First Second Third",
             0),
            (cmd,
                "First Second Third",
                12),
            (cmd,
                "First Second Third",
                18),
        ]
        for cmd, text, p in tests:
            t_line = lineobj.ReadLineTextBuffer(text, p)
            self.assertEqual(p, cmd(t_line))


# ----------------------------------------------------------------------
# utility functions

def get_point_pos(pstr):
    return pstr.index("#")


def get_mark_pos(mstr):
    try:
        return mstr.index("#")
    except ValueError:
        return -1
# ----------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()
