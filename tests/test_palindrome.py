import pytest
from func import palindrome

@pytest.mark.parametrize(
    'x, exp',
    [
        [1, True],
        [121, True],
        [132, False],
        [-1, False],
    ]
)

def test_positive(x, exp):
    res = palindrome.is_palindrome(x)

    assert res == exp, f"expected: {exp}, res: {res}"

@pytest.mark.parametrize(
    'x, expected',
    [
        ['0', TypeError],
    ]
)

def test_negative(x, expected):
    with pytest.raises(expected):
        palindrome.is_palindrome(x)