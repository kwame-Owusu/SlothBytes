"""
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
Notes:
  -using hashmap/dict to store the complements then adding the val as the index in the hashmap. 
"""

def two_sum(nums: int, target: int) -> int:
    hashmap = {}
    for i, val in enumerate(nums):
      complement = target - val
      if complement in hashmap:
         return [hashmap[complement], i]
      hashmap[val] = i
    return -1

nums = [2, 7, 11, 15] 
target = 9
nums2 = [3, 2, 4]
target2 = 6
nums3 = [-1, -2, -3, -4, -5]
target3 = -7
print(two_sum(nums, target))
print(two_sum(nums2, target2))
print(two_sum(nums3, target3))
