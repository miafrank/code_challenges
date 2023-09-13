from typing import List
from itertools import product
from functools import reduce
# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
# Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons)
# is given below. Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]

# Solution:
# Create dictionary where number is key and value is letters
# Get the value for each digit
# May need to merge those two lists
# Use itertools.combionations(digits, digits_len) to generate all possible combos
# Return result

# Validation:
# All digits are between 2-9
# All digits are numeric
# If digit len is zero return empty list


def is_digits_numeric(digits):
    return str.isnumeric(digits)


def is_digits_in_range(digits):
    digit_range = list(range(2, 10))
    digits_in_range = ([digit for digit in digits if int(digit) in digit_range])
    return len(digits) == len(digits_in_range)


def is_digit_len_greater_than_or_equal_to_one(digits):
    return len(digits) >= 1


def letter_combinations(digits: str) -> List[str]:
    valid_digit = (is_digits_numeric(digits)
                   and is_digits_in_range(digits)
                   and is_digit_len_greater_than_or_equal_to_one(digits))
    if not valid_digit:
        return []

    phone_digits_and_letters = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k, l"],
        "6": ["m", "n, o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    digit_to_letter_conversion = [phone_digits_and_letters.get(digit) for digit in digits]

    return ["".join(p) for p in product(*digit_to_letter_conversion)]
