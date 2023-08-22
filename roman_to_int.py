# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together.
# 12 is written as XII, which is simply X + II.
# 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Solution:
# Create a dictionary with the roman numerals and their corresponding values
# Create roman numeral matches/converstions (IV -> 4 NOT 6)
# Create a variable to hold the sum of the roman numerals
# If match is found remove from string and add to total sum
# If match is not found add corresponding value to total sum
# Return the sum
def roman_to_int(roman_numeral: str):
    not_found = - 1
    roman_numeral_sum = 0
    roman_numeral_result = roman_numeral
    roman_to_int_translation = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    four_roman_numeral = "IV"
    nine_roman_numeral = "IX"
    forty_roman_numeral = "XL"
    ninty_roman_numeral = "XC"
    four_hundred_roman_numeral = "CD"
    nine_hundred_roman_numeral = "CM"

    four_found = roman_numeral_result.find(four_roman_numeral)
    if four_found != not_found:
        roman_numeral_result = roman_numeral_result.replace(four_roman_numeral, "")
        roman_numeral_sum += (roman_to_int_translation.get("V")
                              - roman_to_int_translation.get("I"))

    nine_found = roman_numeral_result.find(nine_roman_numeral)
    if nine_found != not_found:
        roman_numeral_result = roman_numeral_result.replace(nine_roman_numeral, "")
        roman_numeral_sum += (roman_to_int_translation.get("X")
                              - roman_to_int_translation.get("I"))

    forty_found = roman_numeral_result.find(forty_roman_numeral)
    if forty_found != not_found:
        roman_numeral_result = roman_numeral_result.replace(forty_roman_numeral, "")
        roman_numeral_sum += (roman_to_int_translation.get("L")
                              - roman_to_int_translation.get("X"))

    ninty_found = roman_numeral_result.find(ninty_roman_numeral)
    if ninty_found != not_found:
        roman_numeral_result = roman_numeral_result.replace(ninty_roman_numeral, "")
        roman_numeral_sum += (roman_to_int_translation.get("C")
                              - roman_to_int_translation.get("X"))

    four_hundred_found = roman_numeral_result.find(four_hundred_roman_numeral)
    if four_hundred_found != not_found:
        roman_numeral_result = roman_numeral_result.replace(four_hundred_roman_numeral, "")
        roman_numeral_sum += (roman_to_int_translation.get("D")
                              - roman_to_int_translation.get("C"))

    nine_hundred_found = roman_numeral_result.find(nine_hundred_roman_numeral)
    if nine_hundred_found != not_found:
        roman_numeral_result = roman_numeral_result.replace(nine_hundred_roman_numeral, "")
        roman_numeral_sum += (roman_to_int_translation.get("M")
                              - roman_to_int_translation.get("C"))

    return roman_numeral_sum + sum([roman_to_int_translation.get(num) for num in roman_numeral_result])
