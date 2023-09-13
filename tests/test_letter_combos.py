from letter_combos import letter_combinations, is_digits_in_range


def test_letter_combos():
    digits_one = "23"
    digits_two = ""
    digits_three = "2"

    expected_digits_one = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    expected_digits_two = []
    expected_digits_three = ["a", "b", "c"]

    assert letter_combinations(digits_one) == expected_digits_one
    assert letter_combinations(digits_two) == expected_digits_two
    assert letter_combinations(digits_three) == expected_digits_three


def test_is_digits_in_range():
    digits_one = "01"
    digits_two = "29"
    digits_three = "47"

    assert (is_digits_in_range(digits_one)) is False
    assert (is_digits_in_range(digits_two)) is True
    assert (is_digits_in_range(digits_three)) is True


def test_is_digit_valid():
    invalid_digit_one = "00"
    invalid_digit_two = "01"
    invalid_digit_three = "***"

    assert (letter_combinations(invalid_digit_one)) == []
    assert (letter_combinations(invalid_digit_two)) == []
    assert (letter_combinations(invalid_digit_three)) == []
