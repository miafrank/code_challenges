# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of
# the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:
# # Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Example 2:
# Input: n = 2
# Output: false

# Solution:
# If the number is equal to 1 -> return true
# If max recurrsion error -> return false

# Create two variables for the first sq and second sq numbers
# Create function to first_sq **2 + second_sq ** 2
# Check if equal to one
# If not equal to one, use sum of squares to repeat the same process

def is_squared_equal_to_one(total_sq):
    target = 1
    return total_sq == target


def square_two_nums(first_sq, second_sq):
    squared = 2
    return pow(first_sq, squared) + pow(second_sq, squared)


def num_to_list(num):
    nums = [int(single_num) for single_num in str(num)]
    if len(nums) == 1:
        nums.insert(0, 0)

    return nums


def happy_number(num: int):
    nums = num_to_list(num)

    total_sq = 0
    first_sq = nums[0]
    second_sq = nums[1]
    total_sq = square_two_nums(first_sq, second_sq)

    if is_squared_equal_to_one(total_sq):
        return True
    else:
        try:
            return happy_number(total_sq)
        except RecursionError:
            return False
