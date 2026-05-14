# -*- coding: utf-8 -*-
# *****************************************************************************
#     Copyright (C) 2006-2020 Jorgen Stenarson. <jorgen.stenarson@bostream.nu>
#     Copyright (C) 2020 Bassem Girgis. <brgirgis@gmail.com>
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
# *****************************************************************************

import importlib
import os
import warnings
from pkgutil import walk_packages
from typing import Tuple

import pytest

_dir = os.path.abspath(os.path.dirname(__file__))

ALL_PACKAGES = ["pyreadline3", "readline"]

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        _dir,
        "..",
    )
)


def all_modules() -> Tuple[str, ...]:

    def onerror(name: str) -> None:
        warnings.warn(f"Failed to import {name} when expanding module_info fixture")

    modules = [
        w
        for p in ALL_PACKAGES
        for w in walk_packages(
            [os.path.join(PROJECT_ROOT, "src", p)],
            prefix=f"{p}.",
            onerror=onerror,
        )
    ]

    return tuple(m.name for m in modules)


@pytest.mark.parametrize("module_name", all_modules())
def test_loads(module_name: str) -> None:
    if "ironpython" in module_name:
        warnings.warn(f"ignoring IronPython module: {module_name}")
        return

    importlib.import_module(module_name)
