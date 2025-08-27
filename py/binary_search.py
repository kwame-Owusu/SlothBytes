"""
Note: 
Binary search is powerful but can only be conducted on sorted arrays which give O(log n).
otherwise linear search is better which give us O(n).

"""


def binary_search(arr: list[int], target: int) -> int:
    l, r = 0, len(arr) - 1

    while l <=  r:
        mid = l + (r - l) // 2 
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

#test cases
test_arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_target1 = 6
print(binary_search(test_arr1,test_target1)) # output 5
