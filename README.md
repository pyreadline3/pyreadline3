# pyreadline3

![Publish](https://github.com/pyreadline3/pyreadline3/workflows/Publish/badge.svg)
![Test](https://github.com/pyreadline3/pyreadline3/workflows/Test/badge.svg)
[![Downloads](https://static.pepy.tech/personalized-badge/pyreadline3?period=week&units=international_system&left_color=black&right_color=orange&left_text=Last%20Week)](https://pepy.tech/project/pyreadline3)
[![Downloads](https://static.pepy.tech/personalized-badge/pyreadline3?period=month&units=international_system&left_color=black&right_color=orange&left_text=Month)](https://pepy.tech/project/pyreadline3)
[![Downloads](https://static.pepy.tech/personalized-badge/pyreadline3?period=total&units=international_system&left_color=black&right_color=orange&left_text=Total)](https://pepy.tech/project/pyreadline3)

The pyreadline3 package is a modern python implementation of GNU readline functionality it is based on the ctypes based UNC readline package by Gary Bishop. It has been tested for use with <b>windows 10</b> and <b>python 3.9</b> & <b>python 3.10</b>

pyeadline3 works on <b>python version 3.5</b> or <b>above 3.5+</b>

> **Note**
> This is version of [pyreadline](https://github.com/pyreadline/pyreadline), with all the necessary changes required for <b>windows</b> to run this module.

The latest development version is always available at the [PyPi](https://pypi.org/project/pyreadline3)

---

> ### Features:

- Autocomplete in console applications.
- Keyboard text selection and copy/paste.
- Shift-arrowkeys for text selection.
- Control-c can be used for copy activate with allow_ctrl_c(True) in config file.
- Double tapping ctrl-c will raise a KeyboardInterrupt, use ctrl_c_tap_time_interval(x) where x is your preferred tap time window, default 0.3 s.
- Paste pastes first line of content on clipboard.
- ipython_paste, pastes tab-separated data as list of lists or numpy array if all data is numeric.
- paste_mulitline_code pastes multi line code, removing any empty lines.

---

> ### Install Package

<b>1. Install from PyPi</b>

```
pip install pyreadline3
```

<b>2. Install from git repository</b>

```
git clone https://github.com/athrvvvv/windows-readline.git](https://github.com/pyreadline3/pyreadline3.git
git cd pyreadline3
python -m pip install https://codeload.github.com/pyreadline3/pyreadline3/tar.gz/refs/tags/v3.4.1
```

> **Warning**
> Make sure python is added to path variable.

---

> ### Contributing

```
git clone https://github.com/athrvvvv/windows-readline.git](https://github.com/pyreadline3/pyreadline3.git
git cd pyreadline3
git push -f origin master
```

---

> ### Building package

```
git clone https://github.com/athrvvvv/windows-readline.git](https://github.com/pyreadline3/pyreadline3.git
git cd pyreadline3
python setup.py sdist bdist_wheel
```

> **Warning**
> Make sure python is added to path variable.
