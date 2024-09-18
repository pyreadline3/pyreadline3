# pyreadline3

[![PyPi Badge](https://img.shields.io/pypi/v/pyreadline3)](https://pypi.org/project/pyreadline3/) 
![Publish](https://github.com/pyreadline3/pyreadline3/workflows/Publish/badge.svg)
![Test](https://github.com/pyreadline3/pyreadline3/workflows/Test/badge.svg)
[![Downloads](https://static.pepy.tech/personalized-badge/pyreadline3?period=week&units=international_system&left_color=black&right_color=orange&left_text=Last%20Week)](https://pepy.tech/project/pyreadline3)
[![Downloads](https://static.pepy.tech/personalized-badge/pyreadline3?period=month&units=international_system&left_color=black&right_color=orange&left_text=Month)](https://pepy.tech/project/pyreadline3)
[![Downloads](https://static.pepy.tech/personalized-badge/pyreadline3?period=total&units=international_system&left_color=black&right_color=orange&left_text=Total)](https://pepy.tech/project/pyreadline3)

The `pyreadline3` package is based on the stale package `pyreadline` located
[here](https://github.com/pyreadline/pyreadline).
The original `pyreadline` package is a Python implementation of GNU `readline`
functionality.
It is based on the `ctypes` based UNC `readline` package by Gary Bishop.
It is not complete.
It has been tested for use with Windows 10.

Version 3.4+ of pyreadline3 runs on Python 3.8+.

`pyreadline3` is available on PyPI and can be installed with

    pip install pyreadline3


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

## Development

To clone the library for development:

    git clone git@github.com:pyreadline3/pyreadline3.git

or 

    git clone https://github.com/pyreadline3/pyreadline3.git

### Build The Virtual Environment

The current earliest Python version supported is `3.8`. You need to be able to create a virtual environment at this version to make sure any changes you make is combatible.

If you are using `conda`:

    conda create --prefix=.venv python=3.8 --yes

If you are using `venv`, make sure you have the right base package:

    >> python --version
    Python 3.8.x

Once you verify your base Python, you can then create a virtual environment using:


    virtualenv -p py3.8 .venv

### Setup

Once you have created your virtual environment and made sure it is active in your current command line:

    pip install -e .[dev]

This should all the dependencies you need for developing into the library and also allow you to run the unit tests:

    pytest

### Debugging 
