"""
Write a function that sorts each string in a list by the letter in alphabetic ascending order (a-z). 
NOTES: 
    -Each string will only have one (lowercase) letter.
    -If given an empty list, return an empty list.
"""
def sort_by_letter(arr: list[str]) -> list:
    if len(arr) == 0:
        return []
     #helper function to extract the first letter from a string
    def first_letter(s: str) -> str:
        for char in s:
            if char.isalpha():
                return char
        return ""
    return sorted(arr, key=first_letter)

print(sort_by_letter(["932c","832u32","2344b"]))
print(sort_by_letter(["99a", "78b", "c2345", "11d"]))
print(sort_by_letter(["572z", "5y5", "304q2"]))
print(sort_by_letter([]))

