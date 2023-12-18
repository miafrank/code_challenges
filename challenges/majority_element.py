# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.
# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Solution: 
# Create dictionary where k is the number and v is the amount of times it appears
# Return the k with the highest value

from typing import List


def majority_element(self, nums: List[int]) -> int:
    nums_count = {}
    acc = 1
    for num in nums:
        if num in nums_count: 
            num_value = nums_count.get(num)
            nums_count[num] = acc + num_value
        else:
            nums_count[num] = 1
    return max(nums_count, key=lambda k: nums_count.get(k))

print(majority_element(nums = [3,2,3]))
print(majority_element(nums = [2,2,1,1,1,2,2]))