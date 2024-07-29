def binary_search_first_occurence(arr: list[int], target: int) -> int:
  low = 0
  high = len(arr) -1 
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return arr.index(arr[mid])
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid -1
  return -1


arr1 = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target1 = 3
arr2 = [2, 3, 5, 7, 11, 13, 17, 19]
target2 = 6
arr3 = [1,2,3,4,5,6,7,7,7,7,8,9,10]
target3 = 7
print(f"First occurence of target is at index: {binary_search_first_occurence(arr1, target1)}")
print(f"First occurence of target is at index: {binary_search_first_occurence(arr2, target2)}")
print(f"First occurence of target is at index: {binary_search_first_occurence(arr3, target3)}")
      