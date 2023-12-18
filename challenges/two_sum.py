from typing import List

# Given an array of integers nums and an integer target, return indices
# of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Solution:
# Validate if first index is equal to target. If so, return [0]
# Create dict of values excluding current index:
# [{ sum_amount: 2, original_index: 1 }, { sum_amount: 4, original_index: 2 }]
# Create function that takes current value and iterate over dict
# and validate if current value is equal to target
# If equal to target return original index in list


def is_target_match(target, current_num_index_value, sum_match_value):
    return current_num_index_value + sum_match_value == target


def sum_current_index_with_nums(target: int,
                                nums_with_original_index: List[dict],
                                current_num_index: int,
                                current_num_index_value: int):
    sum_values = {}

    for num in range(len(nums_with_original_index)):
        target_match = is_target_match(target,
                                       current_num_index_value,
                                       nums_with_original_index[num].get('sum_amount'))
        if (
                nums_with_original_index[num]['original_index'] != current_num_index
                and target_match):
            sum_values = {'sum_match_index': nums_with_original_index[num]
                          .get('original_index'),
                          'current_num_index': current_num_index,
                          'is_target_match': target_match}

            sum_match_index = sum_values.get('sum_match_index')
            current_num_index = sum_values.get('current_num_index')
            return sorted([sum_match_index, current_num_index])
    return sum_values


def two_sum(nums: List[int], target: int):
    nums_with_original_index = [{'sum_amount': nums[num], 'original_index': num}
                                for num in range(len(nums))]
    for num in range((len(nums))):
        match = sum_current_index_with_nums(
            target,
            nums_with_original_index,
            current_num_index=num,
            current_num_index_value=nums[num])
        if match:
            return match

        sum_current_index_with_nums(
            target, nums_with_original_index,
            current_num_index=num,
            current_num_index_value=nums[num])
