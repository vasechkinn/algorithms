import pytest
import func.factorial as factorial

@pytest.mark.parametrize(
    'n, exp, res',
    [
        [3, 6, 6],
        [0, 1, 1],
        
    ]
)

def test_positive(n, exp, res):
    res = factorial.factorial(n)
    assert res == exp, f"expected: {exp}, res: {res}"

def test_negative_valueerror():
    n = -1

    with pytest.raises(ValueError):
        factorial.factorial(n)

def test_negative_typeerror():
    n = '1'

    with pytest.raises(TypeError):
        factorial.factorial(n)