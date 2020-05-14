import pytest

@pytest.mark.parametrize(
    "inicial, some, total",
    [
        (10, 2, 12),
        (0, 3, 3),
        (5, 4, 9),
    ],
)
def test_formula_parsing(inicial, some, total):
    sum = inicial + some
    assert sum == total