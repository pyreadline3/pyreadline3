# pyreadline3

![Publish](https://github.com/pyreadline3/pyreadline3/workflows/Publish/badge.svg)
![Test](https://github.com/pyreadline3/pyreadline3/workflows/Test/badge.svg)
[![Downloads](https://static.pepy.tech/personalized-badge/pyreadline3?period=week&units=international_system&left_color=black&right_color=orange&left_text=Last%20Week)](https://pepy.tech/project/pyreadline3)
[![Downloads](https://static.pepy.tech/personalized-badge/pyreadline3?period=month&units=international_system&left_color=black&right_color=orange&left_text=Month)](https://pepy.tech/project/pyreadline3)
[![Downloads](https://static.pepy.tech/personalized-badge/pyreadline3?period=total&units=international_system&left_color=black&right_color=orange&left_text=Total)](https://pepy.tech/project/pyreadline3)

The `pyreadline3` package is based on the stale package `pyreadline` located
[here](https://github.com/pyreadline/pyreadline).
The original `pyreadline` package is a python implementation of GNU `readline`
functionality.
It is based on the `ctypes` based UNC `readline` package by Gary Bishop.
It is not complete.
It has been tested for use with Windows 10.

Version 3.4+ of pyreadline3 runs on Python 3.5+.

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
[repository](https://github.com/pyreadline3/pyreadline3)
