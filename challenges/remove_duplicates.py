# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two
# elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores)

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first
# five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores)

# Solution # 1
# Iterate through each number in list
# Validate if the number at next index is different
# If next index is the same, append "_" to end of list and remove from list

# Solution # 2
# Create a dictionary where key is number and value is number of times it appears in list
# Create list where dict value > 1
# Get sum, that will be the "_" indicating number of times number repeats
# Return new list list [sorted(dict keys) + "_"]
# Tests
# Values with no repeating numbers is the same as the input
# Values with repeating numbers, appends "_" when there are dupes
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_counter = {}
        acc = 1

        for num_index in range(len(nums)):
            if nums[num_index] in nums_counter:
                num_value = nums_counter.get(nums[num_index])
                nums_counter[nums[num_index]] = acc + num_value
            else:
                nums_counter[nums[num_index]] = acc
        return sorted(list(nums_counter.keys()))


nums1 = [1, 1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

solution = Solution()
assert (solution.removeDuplicates(nums2)) == [0, 1, 2, 3, 4]


k = solution.removeDuplicates(nums1)
assert k == [1, 2]
for i in k:
    assert nums1[i] == nums1[i]

print(solution.removeDuplicates(nums1)) == [1, 2]
