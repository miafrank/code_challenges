from typing import List


def filter_nums_less_than_one(nums: List[int]): 
    return list(filter(lambda n: n >= 1, nums))

def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    nums1 = filter_nums_less_than_one(nums1)
    nums2 = filter_nums_less_than_one(nums2)
    for num in nums2: 
        nums1.append(num)
    return sorted(nums1)    
    

print(merge(nums1=[1,2,3,0,0,0], m= 3, nums2=[2, 5, 6], n=3))
print(merge(nums1=[1], m=1, nums2=[], n=0))
print(merge(nums1=[0], m=0, nums2=[1], n=1))
