import pytest
import inspect
from assignment import print_even_numbers, reverse_number, sum_of_n_numbers, is_prime, print_perfect_squares


def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source


# Exercise 1 (Print even numbers)
def test1(capsys):
    print_even_numbers()
    captured = capsys.readouterr()
    output = captured.out.strip().split()
    expected = list(map(str, range(2, 51, 2)))
    assert output == expected
    assert check_contains_loop(print_even_numbers)


# Exercise 2 (Reverse number)
@pytest.mark.parametrize("num, expected", [
    (1234, 4321),
    (907, 709),
    (5, 5),
    (1000, 1),
    (0, 0)
])
def test2(num, expected):
    assert reverse_number(num) == expected
    assert check_contains_loop(reverse_number)


# Exercise 3 (Sum of numbers 1..n)
@pytest.mark.parametrize("num, expected", [
    (5, 15),
    (10, 55),
    (1, 1),
    (0, 0),
    (7, 28)
])
def test3(num, expected):
    assert sum_of_n_numbers(num) == expected
    assert check_contains_loop(sum_of_n_numbers)


# Exercise 4 (Prime check)
@pytest.mark.parametrize("num, expected", [
    (7, True),
    (12, False),
    (1, False),
    (2, True),
    (29, True),
    (30, False)
])
def test4(num, expected):
    assert is_prime(num) == expected
    assert check_contains_loop(is_prime)


# Exercise 5 (Print perfect squares up to 500)
def test5(capsys):
    print_perfect_squares()
    captured = capsys.readouterr()
    output = captured.out.strip().split()
    expected = [str(i * i) for i in range(1, 23) if i * i <= 500]
    assert output == expected
    assert check_contains_loop(print_perfect_squares)
