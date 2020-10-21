# pyreadline3

The `pyreadline3` package is based on the stale package `pyreadline` located
[here](https://github.com/pyreadline/pyreadline).
The original `pyreadline` package is a python implementation of GNU `readline`
functionality.
It is based on the `ctypes` based UNC `readline` package by Gary Bishop.
It is not complete.
It has been tested for use with Windows 10.

Version 3.0+ of pyreadline3 runs on Python 3.8+.

## Features

- keyboard text selection and copy/paste
- Shift-arrowkeys for text selection
- Control-c can be used for copy activate with allow_ctrl_c(True) in config file
- Double tapping ctrl-c will raise a KeyboardInterrupt, use ctrl_c_tap_time_interval(x)
- where x is your preferred tap time window, default 0.3 s.
- paste pastes first line of content on clipboard.
- ipython_paste, pastes tab-separated data as list of lists or numpy array if all data is numeric
- paste_mulitline_code pastes multi line code, removing any empty lines.

The latest development version is always available at the project git
[repository](https://github.com/brgirgis/pyreadline3)
