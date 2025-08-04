import pytest
from func import sum_elems

@pytest.mark.parametrize(
    'arr, exp',
    [
        [[4, 3, 2, 1], [4, 3, 2, 2]],
        [[9], [1, 0]],
        [[1, 2, 3, 4, 5], [1, 2, 3, 4, 6]],
        [[0], [1]],
        [[0, 0, 0], [1]],
        [[9, 0, 9], [9, 1, 0]],
    ]
)
def test_positive(arr, exp):
    res = sum_elems.amount_plus_1(arr)

    assert res == exp, f"exp: {exp}, res: {res}"


@pytest.mark.parametrize(
    'arr, exp',
    [
        [[], ValueError],
        ["[5, 4, 3, 2, 4, 8]", TypeError],
        [1, TypeError],
    ]
)

def test_negative(arr, exp):
    with pytest.raises(exp):
        sum_elems.amount_plus_1(arr)