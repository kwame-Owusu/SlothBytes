"""
Return the coordinates ([row, col]) of the element that differs from the rest.
Notes: 
    -The given array will always be a square or rectangle.
    -Rows and columns are 1-indexed (not zero-indexed).
"""

def where_is_waldo(arr: list[list[str]]) -> list[int]:
    first_element = arr[0][0]
    for row in range(len(arr)):
        for col in range(len(arr[row])):
         if arr[row][col] != first_element:
           return [row + 1, col + 1] #because rows and cols have to be 1-indexed
    return -1, -1 # if all elements are the same
            

test = [
  ["A", "A", "A"],
  ["A", "A", "A"],
  ["A", "B", "A"]
]

test2 = [
  ["c", "c", "c", "c"],
  ["c", "c", "c", "d"]
]

test3 = [
    ["Waldo", "Waldo", "Waldo"],
    ["Waldo", "Waldo", "Waldo"],
    ["Waldo", "Waldo", "not Waldo"]
]

test4 = [
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["O", "O", "O", "O"],
  ["P", "O", "O", "O"],
  ["O", "O", "O", "O"]
]
print(where_is_waldo(test))
print(where_is_waldo(test2))
print(where_is_waldo(test3))
print(where_is_waldo(test4))
