import sys
import pytest
from linetable import generate_linetable, parse_linetable


def test_parse_linetable():
    linetable = b"\x80\x00\xd8\x06\x07\x80!\xd8\x06\x07\x88!\x81e\x80!\xd8\t\n\x80("
    parsed = list(parse_linetable(linetable))
    assert parsed == [
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


def test_parse_linetable_nocolumns():
    linetable = (
        b"\xe8\x00\xe8\x02\xe8\x00\xe8\x02\xe8\x00\xe9\x00\xe8\x00\xe8\x02\xe8\x00"
    )
    parsed = list(parse_linetable(linetable))
    assert parsed == [
        (1, 1, 1, None, None),
        (1, 2, 2, None, None),
        (1, 2, 2, None, None),
        (1, 3, 3, None, None),
        (1, 3, 3, None, None),
        (2, 3, 3, None, None),
        (1, 3, 3, None, None),
        (1, 4, 4, None, None),
        (1, 4, 4, None, None),
    ]


def test_linetable():
    pairs = [
        # length, start_line, end_line, start_col, end_col
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
    expected = b"\x80\x00\xd8\x06\x07\x80!\xd8\x06\x07\x88!\x81e\x80!\xd8\t\n\x80("
    assert generate_linetable(pairs, use_bytecode_offset=False) == expected


def test_linetable_offsets():
    pairs = [
        # bytecode_offset, start_line, end_line, start_col, end_col
        (0, 1, 1, 0, 0),
        (2, 2, 2, 6, 7),
        (4, 2, 2, 2, 3),
        (6, 3, 3, 6, 7),
        (8, 3, 3, 10, 11),
        (10, 3, 3, 6, 11),
        (14, 3, 3, 2, 3),
        (16, 4, 4, 9, 10),
        (18, 4, 4, 2, 10),
    ]
    expected = b"\x80\x00\xd8\x06\x07\x80!\xd8\x06\x07\x88!\x81e\x80!\xd8\t\n\x80("
    assert generate_linetable(pairs, use_bytecode_offset=True) == expected


def test_linetable_offsets_short():
    pairs = [
        # bytecode_offset, linenum
        (0, 1),
        (2, 2),
        (4, 2),
        (6, 3),
        (8, 3),
        (10, 3),
        (14, 3),
        (16, 4),
        (18, 4),
    ]
    expected = (
        b"\xe8\x00\xe8\x02\xe8\x00\xe8\x02\xe8\x00\xe9\x00\xe8\x00\xe8\x02\xe8\x00"
    )
    assert generate_linetable(pairs, use_bytecode_offset=True) == expected


@pytest.mark.skipif(sys.version_info < (3,11),
                    reason="requires python3.11+")
def test_roundtrip():
    def _test_function():
        x = 13
        y = x * 2 + 7 + 8 + 9 - 3 - 1 - 5
        z = y**2
        return z

    co_linetable = _test_function.__code__.co_linetable
    assert (
        generate_linetable(
            parse_linetable(generate_linetable(parse_linetable(co_linetable)))
        )
        == co_linetable
    )
