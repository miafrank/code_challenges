from two_sum_code_challenge import two_sum


def test_two_sum():
    nums1 = [2, 7, 11, 15]
    nums2 = [3, 3]
    nums3 = [3, 2, 4]
    nums4 = [0, 4, 3, 0]

    target1 = 9
    target2 = 6
    target3 = 6
    target4 = 0

    expected1 = [0, 1]
    expected2 = [0, 1]
    expected3 = [1, 2]
    expected3 = [1, 2]
    expected4 = [0, 3]

    assert (two_sum(nums1, target1)) == expected1
    assert (two_sum(nums2, target2)) == expected2
    assert (two_sum(nums3, target3)) == expected3
    assert (two_sum(nums4, target4)) == expected4
