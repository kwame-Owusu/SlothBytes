"""
Given a list of integers, remove all duplicate values and return a list with only unique elements. The order of the elements should be preserved.
Notes: 
  -keep track of the elements by using a hashmap and if the count of said element it more than one, dont add to the new list to return.
"""
def remove_duplicates(nums: list[int]) -> list[int]:
    
    count = {}
    for i in nums:
      if i in count:
        count[i] += 1
      else:
         count[i] = 1
        
        
    result = []
    for num in nums:
        if count[num] == 1:
          result.append(num)
    return result

test = [1, 2, 2, 3, 4, 4, 5]
test2 = [1,1,2,3,3,4,4,5,10]
print(remove_duplicates(test)) # returns [1, 3, 5]
print(remove_duplicates(test2))# returns [2, 5, 10]

