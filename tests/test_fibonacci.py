import pytest
from func import fibonacci

@pytest.mark.parametrize(
    'n, exp',
    [
        [1, [0, 1]],
        [0, [0]],
        [13, [0, 1, 1, 2, 3, 5, 8, 13]]
    ]
)

def test_positive(n, exp):
    res = fibonacci.fibonacci(n)

    assert res == exp, f"expected: {exp}, res: {res}"

@pytest.mark.parametrize(
    'n, expected',
    [
        [-1, ValueError],
        ['0', TypeError],
    ]
)

def test_negative(n, expected):
    with pytest.raises(expected):
        fibonacci.fibonacci(n)