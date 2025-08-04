import pytest
from func import rotate

@pytest.mark.parametrize(
    'arr, k, exp',
    [
        [[1, 2, 3, 4, 5], 2, [3, 2, 1, 5, 4]],
        [[1], 2, [1]],
        [[1, 2, 3, 4, 5], 5, [5, 4, 3, 2, 1]],
        [[1, 2, 3, 4, 5], 0, [5, 4, 3, 2, 1]],
    ]
)
def test_positive(arr, k, exp):
    res = rotate.rotate_and_reverse(arr, k)

    assert res == exp, f"exp: {exp}, res: {res}"


@pytest.mark.parametrize(
    'arr, k, exp',
    [
        [[5, 4, 3, 2, 4, 8], -1, ValueError],
        ["[5, 4, 3, 2, 4, 8]", 5, TypeError],
        [[5, 4, 3, 2, 4, 8], '2', TypeError],
        ['[5, 4, 3, 2, 4, 8]', '15', TypeError],
    ]
)

def test_negative(arr, k, exp):
    with pytest.raises(exp):
        rotate.rotate_and_reverse(arr, k)