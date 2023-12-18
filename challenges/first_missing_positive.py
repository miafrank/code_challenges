from typing import List

# Solution - Given an unsorted integer array nums, return the smallest missing positive integer
# Example:
# Input: nums = [1,2,0] sorted([0, 1, 2])
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# 1. Sort nums list and check if first number in list is 0
# 2. Iterate over each number in list to verify if [current_index + 1] == +1 of current_index
#       - If first number is 0 and next number is NOT 1 -> return 1
#       - If current_index_value + 1 == 0:
#               - Do nothing, go to next index
#       - If sorted numbers in list are all +1 the value and first index value is 1
#               -> return (arr[::-1] + 1)
#
#       example: sorted([-1, 1, 3, 4])
#       - If sorted numbers in list NOT all +1:
#              - return (next_index_value - current_index_value)
#               example: # sorted([-3, -2, -1, 0, 4])
#               - Filter out numbers <= 0 and sort
#               - [4] Check if list[0] is equal to 1
#               - If not return 1


class Solution:
    def sorted_nums_positive(self, sorted_nums: List[int]) -> List[int]:
        return list(filter((lambda x: x >=1), sorted_nums))

    def find_missing_number(self, sorted_positive_numbers: List[int]) -> List[int]:
        print(sorted_positive_numbers)
        next_index = 1 # [1, 2, 5, 6]
        result = [print(num_index) for num_index in range(len(sorted_positive_numbers))
                  if sorted_positive_numbers[num_index] + 1
                  != sorted_positive_numbers[num_index + next_index]]
        return result

    def firstMissingPositive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        sorted_nums_next_value_equals_one = []
        smallest_possible_positive = 1
        zero = 0
        next_index = 1

        for nums_index in range(len(sorted_nums)):
            end_of_search = nums_index == (len(sorted_nums) - 1)
            # print(end_of_search)

            if not end_of_search and sorted_nums[nums_index] + 1 == zero:
                nums_index += next_index
            if (
                not end_of_search
                and sorted_nums[nums_index] + 1 == sorted_nums[nums_index + next_index]
            ):
                sorted_nums_next_value_equals_one.append(True)
            if (
                not end_of_search
                and sorted_nums[nums_index] + 1 != sorted_nums[nums_index + next_index]
            ):
                sorted_nums_next_value_equals_one.append(False)

            if (
                not end_of_search
                and sorted_nums[nums_index] == zero
                and sorted_nums[nums_index + next_index] != 1
            ):
                return smallest_possible_positive

            if end_of_search:
                if (
                    any(sorted_nums_next_value_equals_one)
                    and smallest_possible_positive in sorted_nums
                ):
                    # [-3, -1, 1, 2, 5, 6]
                    sorted_nums_positive_ints = self.sorted_nums_positive(sorted_nums)
                    if sorted_nums_positive_ints[0] != 1:
                        return smallest_possible_positive
                    else:
                        return self.find_missing_number(sorted_nums_positive_ints)
                if (
                    all(sorted_nums_next_value_equals_one)
                    and smallest_possible_positive in sorted_nums
                ):
                    return sorted_nums[-1] + 1
                if (
                    all(sorted_nums_next_value_equals_one)
                    and smallest_possible_positive not in sorted_nums
                ):
                    return smallest_possible_positive

                if (
                    any(sorted_nums_next_value_equals_one)
                    and smallest_possible_positive not in sorted_nums
                ):
                    return smallest_possible_positive


solution = Solution()
# assert solution.firstMissingPositive([0, 2]) == 1
# assert solution.firstMissingPositive([1, 2, 0]) == 3
print(solution.firstMissingPositive([3, 4, -1, 1]))  # 2
# assert solution.firstMissingPositive([7, 8, 9, 11, 12]) == 1
# assert solution.firstMissingPositive([-3, -2, -1, 0, 4]) == 1
