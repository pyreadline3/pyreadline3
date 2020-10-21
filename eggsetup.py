# -*- coding: utf-8 -*-

# *****************************************************************************
#       Copyright (C) 2006  Jorgen Stenarson. <jorgen.stenarson@bostream.nu>
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
# *****************************************************************************
import glob

from setuptools import find_packages, setup

exec(
    compile(
        open('pyreadline3/release.py').read(),
        'pyreadline3/release.py',
        'exec'))

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
    #      download_url     = download_url,
    platforms=platforms,
    keywords=keywords,
    py_modules=['readline'],
    packages=['pyreadline3'],
    data_files=[('doc', glob.glob("doc/*")),
                ],
    zip_safe=False,
)
