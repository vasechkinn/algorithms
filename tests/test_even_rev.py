import pytest
from func import reverse_even

@pytest.mark.parametrize(
    'arr, exp',
    [
        [[1, 2, 3, 4, 5, 6, 8], [1, 8, 3, 6, 5, 4, 2]],
        [[1], [1]],
        [[1, 3, 5], [1, 3, 5]],
        [[2, 4, 6], [6, 4, 2]],
        [[1, 2, 3, 4], [1, 4, 3, 2]]
    ]
)
def test_positive(arr, exp):
    res = reverse_even.reverse_even_elements(arr)

    assert res == exp, f"exp: {exp}, res: {res}"


@pytest.mark.parametrize(
    'arr, exp',
    [
        ["[5, 4, 3, 2, 4, 8]", TypeError],
        [[], ValueError],
        [0, TypeError]
    ]
)

def test_negative(arr, exp):
    with pytest.raises(exp):
        reverse_even.reverse_even_elements(arr)