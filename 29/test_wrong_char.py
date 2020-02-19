from wrong_char import get_index_different_char
import pytest

@pytest.mark.parametrize("input_list, expected", [
        (['A', 'f', '.', 'Q', 2], 2),
        (['.', '{', ' ^', '%', 'a'], 4),
        ([1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'], 1),
        (['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'], 5),
        (list(range(1,9)) + ['}'] + list('abcde'), 8),  # noqa E230
        ([2, '.', ',', '!'], 0),
        ])
def test_wrong_char(input_list, expected):

    err = f'get_index_different_char({input_list}) should return index {expected}'
    assert get_index_different_char(input_list) == expected #, err