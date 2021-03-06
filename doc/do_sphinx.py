#!/usr/bin/env python
"""Script to build documentation using Sphinx.
"""

import fileinput
import os
import sys


def oscmd(c):
    os.system(c)


if os.path.isdir("build"):
    os.removedirs("build")

os.makedirs("build/html")
os.makedirs("build/latex")

# html manual.
oscmd('sphinx-build -d build/doctrees source build/html')

if sys.platform != 'win32':
    # LaTeX format.
    oscmd('sphinx-build -b latex -d build/doctrees source build/latex')

    # Produce pdf.
    topdir = os.getcwd()
    os.chdir('build/latex')

    # Change chapter style to section style: allows chapters to start on
    # the current page.  Works much better for the short chapters we have.
    # This must go in the class file rather than the preamble, so we modify
    # manual.cls at runtime.
    chapter_cmds = r'''
% Local changes.
\renewcommand\chapter{
    \thispagestyle{plain}
    \global\@topnum\z@
    \@afterindentfalse
    \secdef\@chapter\@schapter
}
\def\@makechapterhead#1{
    \vspace*{10\p@}
    {\raggedright \reset@font \Huge \bfseries \thechapter \quad #1}
    \par\nobreak
    \hrulefill
    \par\nobreak
    \vspace*{10\p@}
}
\def\@makeschapterhead#1{
    \vspace*{10\p@}
    {\raggedright \reset@font \Huge \bfseries #1}
    \par\nobreak
    \hrulefill
    \par\nobreak
    \vspace*{10\p@}
}
'''

    unmodified = True
    for line in fileinput.FileInput('manual.cls', inplace=1):
        if 'Support for module synopsis' in line and unmodified:
            line = chapter_cmds + line
        elif 'makechapterhead' in line:
            # Already have altered manual.cls: don't need to again.
            unmodified = False
        print(line)

    # Copying the makefile produced by sphinx...
    oscmd('pdflatex pyreadline3.tex')
    oscmd('pdflatex pyreadline3.tex')
    oscmd('pdflatex pyreadline3.tex')
    oscmd('makeindex -s python.ist pyreadline3.idx')
    oscmd('makeindex -s python.ist modpyreadline.idx')
    oscmd('pdflatex pyreadline3.tex')
    oscmd('pdflatex pyreadline3.tex')

    # Create a manual/ directory with final html/pdf output
#    os.chdir(topdir)
#    oscmd('rm -rf manual')
#    oscmd('mkdir manual')
#    oscmd('cp -r build/html/*.html build/html/_static manual/')
#    oscmd('cp build/latex/ipython.pdf manual/')
