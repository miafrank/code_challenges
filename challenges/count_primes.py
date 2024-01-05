# Given an integer n, return the number of prime numbers that are
# strictly less than n

# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Example 2:
# Input: n = 0
# Output: 0

# Example 3:
# Input: n = 1
# Output: 0

# Solution:
# 2 is the lowest prime number
# First check if input is greater than 2
# If number is 0 or 1 -> return 0
# If > 2 = add to prime_numbers list

# Find all factors of input number:
# If the factors list only contain 1 and itself -> return 0
# Generate factors for input number
# Return len of numbers less than input num

from typing import List


def generate_nums_range(num: int):
    nums = []
    smallest_prime_number = 2
    return nums + list(range(smallest_prime_number, num + 1))


def generate_factors(nums: List[int], input_num: int):
    return [num for num in range(2, input_num + 1)]


def is_prime(input_num):
    prime_value = 2
    prime_number = [num
                    for num in range(1, input_num + 1)
                    if input_num % num == 0]

    return len(prime_number) == prime_value


def find_prime_numbers(factors: List[int]):
    return [num for num in range(2, len(factors) + 1)
            if is_prime(num)]


def count_primes(num: int):
    nums_range = generate_nums_range(num)
    factors = generate_factors(nums=nums_range, input_num=num)

    prime_numbers = find_prime_numbers(factors)

    return len(prime_numbers)
