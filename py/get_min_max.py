def get_max(nums: list[int]) -> int:
    cur_max = nums[0]
    for i in nums:
        if i > cur_max:
            cur_max = i
    return cur_max


def get_min(nums: list[int]) -> int:
    cur_min = nums[0]
    for i in nums:
        if i < cur_min:
            cur_min = i
    return cur_min



def find_index(nums: list[int], target: int) -> list[int]:
    indices = []
    for i, num in enumerate(nums):
        if num == target:
            indices.append(i)
    return indices


print(find_index([10, 2, 5, 6, 8, 2, 2, 0, 1], 2)) 
