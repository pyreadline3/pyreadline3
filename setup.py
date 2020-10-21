# -*- coding: utf-8 -*-

# *****************************************************************************
#       Copyright (C) 2003-2006 Gary Bishop.
#       Copyright (C) 2006-2020 Jorgen Stenarson. <jorgen.stenarson@bostream.nu>
#       Copyright (C) 2020 Bassem Girgis. <brgirgis@gmail.com>
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
# *****************************************************************************

import glob
import os
import sys
from distutils.core import setup
from platform import system

_S = system()
if 'windows' != _S.lower():
    raise RuntimeError('pyreadline3 is for Windows only, not {}.'.format(_S))

# BEFORE importing distutils, remove MANIFEST. distutils doesn't properly
# update it when the contents of directories change.
if os.path.exists('MANIFEST'):
    os.remove('MANIFEST')
#

exec(
    compile(
        open('pyreadline3/release.py').read(),
        'pyreadline3/release.py',
        'exec'))

try:
    import sphinx
    from sphinx.setup_command import BuildDoc
    cmd_class = {'build_sphinx': BuildDoc}
except ImportError:
    cmd_class = {}

packages = [
    'pyreadline3',
    'pyreadline3.clipboard',
    'pyreadline3.configuration',
    'pyreadline3.console',
    'pyreadline3.keysyms',
    'pyreadline3.lineeditor',
    'pyreadline3.modes',
    'pyreadline3.test',
]

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    author=authors["Jorgen"][0],
    author_email=authors["Jorgen"][1],
    maintainer=authors["Jorgen"][0],
    maintainer_email=authors["Jorgen"][1],
    license=license,
    classifiers=classifiers,
    url=url,
    download_url=download_url,
    platforms=platforms,
    keywords=keywords,
    py_modules=['readline'],
    packages=packages,
    package_data={'pyreadline3': ['configuration/*']},
    data_files=[],
    cmdclass=cmd_class
)
