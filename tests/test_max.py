import pytest
from func import max_in_range

@pytest.mark.parametrize(
    'arr, start, end, exp',
    [
        [[5, 4, 3, 2, 4, 8], 1, 4, (0, 1)],
        [[5, 4, 3, 2, 4, 8], 2, 5, (3, 5)],
        [[5, 4, 3, 2, 4, 8], 2, 2, (0, 2)],
    ]
)
def test_positive(arr, start, end, exp):
    res = max_in_range.max_in_range(arr, start, end)

    assert res == exp, f"exp: {exp}, res: {res}"


@pytest.mark.parametrize(
    'arr, start, end, exp',
    [
        [[5, 4, 3, 2, 4, 8], -1, 4, ValueError],
        ["[5, 4, 3, 2, 4, 8]", 2, 5, TypeError],
        [[5, 4, 3, 2, 4, 8], 5, 2, ValueError],
        [[5, 4, 3, 2, 4, 8], 5, 15, ValueError],
        [[5, 4, 3, 2, 4, 8], '5', '2', ValueError],
        [[5, 4, 3, 2, 4, 8], 0, -2, ValueError],
    ]
)

def test_negative(arr, start, end, exp):
    with pytest.raises(exp):
        max_in_range.max_in_range(arr, start, end)