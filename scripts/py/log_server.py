# -*- coding: utf-8 -*-
# *****************************************************************************
#       Copyright (C) 2006-2020 Jorgen Stenarson. <jorgen.stenarson@bostream.nu>
#       Copyright (C) 2020 Bassem Girgis. <brgirgis@gmail.com>
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
# *****************************************************************************


import logging
import logging.handlers
import socket
from typing import Optional

from pyreadline3.unicode_helper import ensure_unicode

try:
    import msvcrt
except ImportError:
    msvcrt = None
    print("problem")


PORT_NUMBER = logging.handlers.DEFAULT_TCP_LOGGING_PORT
HOST_NAME = ""


def check_key() -> Optional[str]:
    if msvcrt is None:
        return None

    if msvcrt.kbhit():
        q = ensure_unicode(msvcrt.getch())
        return q

    return ""


def main() -> None:
    print("Starting TCP log_server on port:", PORT_NUMBER)
    print("Press q to quit log_server")
    print("Press c to clear screen")

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind((HOST_NAME, PORT_NUMBER))
    s.settimeout(1)

    while True:
        try:
            data, _ = s.recvfrom(100000)
            print(data, end="")
        except socket.timeout:
            key = check_key().lower()

            if "q" == key:
                print("Quitting log_server ... bye")
                break

            if "c" == key:
                print("\n" * 100)


if __name__ == "__main__":
    main()
