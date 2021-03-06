# -*- coding: utf-8 -*-

# *****************************************************************************
#       Copyright (C) 2006-2020 Jorgen Stenarson. <jorgen.stenarson@bostream.nu>
#       Copyright (C) 2020 Bassem Girgis. <brgirgis@gmail.com>
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
# *****************************************************************************
import glob

from setuptools import setup

name = 'UNKNOWN'
version = 'NONE'
description = 'NONE'
long_description = 'NONE'
authors = {}
license_name = 'NONE'
classifiers = 'NONE'
url = 'NONE'
platforms = 'NONE'
keywords = 'NONE'

exec(
    compile(
        open('pyreadline3/release.py', 'r', encoding='utf-8').read(),
        'pyreadline3/release.py',
        'exec'
    )
)


setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    author=authors["Bassem"][0],
    author_email=authors["Bassem"][1],
    maintainer=authors["Bassem"][0],
    maintainer_email=authors["Bassem"][1],
    license=license_name,
    classifiers=classifiers,
    url=url,
    platforms=platforms,
    keywords=keywords,
    py_modules=['readline'],
    packages=['pyreadline3'],
    data_files=[('doc', glob.glob("doc/*")),
                ],
    zip_safe=False,
)
