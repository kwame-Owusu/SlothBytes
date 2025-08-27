"""
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
Example 1:

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
"""

def intersection(self, nums: List[List[int]]) -> List[int]:
  hashmap = {}
  result = []

  for i in range(len(nums)):
    for j in nums[i]:
        if j in hashmap:
          hashmap[j] += 1
        else:
          hashmap[j] = 1

  for key, value in hashmap.items():
    if value == len(nums):
      result.append(key)
 return sorted(result))
