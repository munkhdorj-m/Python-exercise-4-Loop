import pytest
import numpy as np
from assignment import greet, perform_operations, check_even_odd, compare_numbers, multiply_digits 


def test1(capsys):
    greet()
    captured = capsys.readouterr()
    assert captured.out.strip().lower() == "hello, world!"
    
def test2():
    assert perform_operations(10, 2) == (12, 8, 20, 5)
    assert perform_operations(5, 5) == (10, 0, 25, 1)
    assert perform_operations(7, 3) == (10, 4, 21, 7/3)

@pytest.mark.parametrize("input, expected", [
    (2, "even"),
    (3, "odd"),
    (0, "even"),
    (-5, "odd")
])
def test3(input, expected):
    assert check_even_odd(input).lower() == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 5),
    (2, 7, 7),
    (4, 4, "equal")
])
def test4(num1, num2, expected):
    result = compare_numbers(num1, num2)
    if isinstance(result, str):
        assert result.lower() == expected.lower()
    else:
        assert result == expected

@pytest.mark.parametrize("input, expected", [(253, 30), (123, 6), (999, 729), (321, 6)])
def test5(input, expected):
    assert multiply_digits(input) == expected
