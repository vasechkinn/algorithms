import pytest
from func import count_ones

@pytest.mark.parametrize(
    'n, exp',
    [
        [150, 4],
        [0, 0],
        [1, 1]
    ]
)

def test_positive(n, exp):
    res = count_ones.count_ones(n)
    assert res == exp, f"expected: {exp}, res: {res}"

@pytest.mark.parametrize(
    'n, exp',
    [
        [-1, ValueError],
        ['1', TypeError],
    ]
)

def test_negative(n, exp):
    with pytest.raises(exp):
        count_ones.count_ones(n)