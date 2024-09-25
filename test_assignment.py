import pytest
from assignment import print_love_python, sum_of_n_numbers, sum_of_digits, count_digits, print_from_five_to

def test_print_love_python(capsys):
    print_love_python()
    captured = capsys.readouterr()
    assert captured.out.strip() == "\n".join(["I Love Python"] * 10)

@pytest.mark.parametrize("input, expected", [
    (5, 15),
    (11, 66),
    (3, 6),
    (0, 0)
])
def test_sum_of_n_numbers(input, expected):
    assert sum_of_n_numbers(input) == expected

@pytest.mark.parametrize("input, expected", [
    (125, 8),
    (5, 5),
    (1234, 10),
    (0, 0)
])
def test_sum_of_digits(input, expected):
    assert sum_of_digits(input) == expected

@pytest.mark.parametrize("input, expected", [
    (123, 3),
    (9, 1),
    (56741, 5),
    (0, 1)
])
def test_count_digits(input, expected):
    assert count_digits(input) == expected

@pytest.mark.parametrize("input, expected", [
    (9, [5, 6, 7, 8, 9]),
    (7, [5, 6, 7]),
    (-2, [5, 4, 3, 2, 1, 0, -1, -2])
])
def test_print_from_five_to(capsys, input, expected):
    print_from_five_to(input)
    captured = capsys.readouterr()
    assert captured.out.strip().splitlines() == list(map(str, expected))
