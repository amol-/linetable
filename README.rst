About linetable
---------------

linetable is a library parse and generate co_linetable attributes in Python code objects.

Installing
----------

linetable can be installed from pypi::

    pip install linetable

should just work for most of the users

Usage
-----

Existing linetable can be parsed using ``linetable.parse_linetable``::

    >>> def testfunc():
    ...   x = 3
    ...   y = x + 1
    ...   return y

    >>> list(linetable.parse_linetable(testfunc.__code__.co_linetable))
    [
        (1, 1, 1, 0, 0),
        (1, 2, 2, 6, 7),
        (1, 2, 2, 2, 3),
        (1, 3, 3, 6, 7),
        (1, 3, 3, 10, 11),
        (2, 3, 3, 6, 11),
        (1, 3, 3, 2, 3),
        (1, 4, 4, 9, 10),
        (1, 4, 4, 2, 10),
    ]

If you prefer the output in the format of ``dis.Positions`` objects,
you can create them from the yielded values::

    >>> [dis.Positions(*e[1:]) for e in linetable.parse_linetable(testfunc.__code__.co_linetable)]
    [Positions(lineno=1, end_lineno=1, col_offset=0, end_col_offset=0), Positions(lineno=2, end_lineno=2, col_offset=8, end_col_offset=9), Positions(lineno=2, end_lineno=2, col_offset=4, end_col_offset=5), Positions(lineno=3, end_lineno=3, col_offset=8, end_col_offset=9), Positions(lineno=3, end_lineno=3, col_offset=12, end_col_offset=13), Positions(lineno=3, end_lineno=3, col_offset=8, end_col_offset=13), Positions(lineno=3, end_lineno=3, col_offset=4, end_col_offset=5), Positions(lineno=4, end_lineno=4, col_offset=11, end_col_offset=12), Positions(lineno=4, end_lineno=4, col_offset=4, end_col_offset=12)]

If you have the linetable, you can generate back the binary encoded version
using ``linetable.generate_linetable``::

    >>> lt = [
    ...     (1, 1, 1, 0, 0),
    ...     (1, 2, 2, 6, 7),
    ...     (1, 2, 2, 2, 3),
    ...     (1, 3, 3, 6, 7),
    ...     (1, 3, 3, 10, 11),
    ...     (2, 3, 3, 6, 11),
    ...     (1, 3, 3, 2, 3),
    ...     (1, 4, 4, 9, 10),
    ...     (1, 4, 4, 2, 10),
    ... ]
    >>> linetable.generate_linetable(lt)
    b"\x80\x00\xd8\x06\x07\x80!\xd8\x06\x07\x88!\x81e\x80!\xd8\t\n\x80("
