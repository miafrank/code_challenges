import challenges.majority_element as majority_element


def test_majority_element():
    assert(majority_element(nums = [3,2,3]) == 3)
    assert(majority_element(nums = [2,2,1,1,1,2,2]) == 2)