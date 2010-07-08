winreg_unicode
==============

The winreg_unicode package is a drop-in replacement for Python 2's
`_winreg`_ module.  However, it returns unicode values where possible,
similar to Python 3's `winreg`_ module.

To illustrate the need for the winreg_unicode package, suppose an
application must query the registry to discover a filename and the
registry contains the string "međuresorna.txt".  Python 2's `_winreg`_
module will return "meduresorna.txt" instead, which is not the actual
name of the file.

The winreg_unicode package does not yet contain all of `_winreg`_'s
functions.  In particular, functions that write to the registry are
not yet included.  Code contributions are welcome.

The following functions *are* included in winreg_unicode:

- `OpenKey`_
- `QueryInfoKey`_
- `EnumValue`_
- `EnumKey`_
- `QueryValueEx`_

.. _`_winreg`: http://docs.python.org/library/_winreg.html
.. _winreg: http://docs.python.org/py3k/library/winreg.html
.. _OpenKey: http://docs.python.org/py3k/library/winreg.html#winreg.OpenKey
.. _QueryInfoKey: http://docs.python.org/py3k/library/winreg.html#winreg.QueryInfoKey
.. _EnumValue: http://docs.python.org/py3k/library/winreg.html#winreg.EnumValue
.. _EnumKey: http://docs.python.org/py3k/library/winreg.html#winreg.EnumKey
.. _QueryValueEx: http://docs.python.org/py3k/library/winreg.html#winreg.QueryValueEx

Relevant links
--------------

- `Bug tracker`_
- `Source code`_

.. _`Bug tracker`: http://github.com/DanielStutzbach/winreg_unicode/issues
.. _`Source code`: http://github.com/DanielStutzbach/winreg_unicode
