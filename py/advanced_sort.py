from typing import Union

def advanced_sort(array:list[Union[int, str]]) -> list[Union[int, str]]:
    grouped_items = {}
    for i in array:
        if i not in grouped_items:
            grouped_items[i] = []
        grouped_items[i].append(i)
    return list(grouped_items.values())

result = advanced_sort([2, 1, 2, 1])
print(result)