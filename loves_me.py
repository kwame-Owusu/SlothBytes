"""
Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, 
and return the last phrase in all caps. Remember to put a comma and space between phrases.

Notes:
  -Remember to return a string.
  -The first phrase is always "Loves me".
"""


def loves_me(num: int) -> str:
    result = []
    for i in range(num):
        if i % 2==0:
            result.append("Loves me")
        else:
            result.append("Loves me not")
        if i == num -1:
            result[-1] = result[-1].upper()
    return ",".join(result) 

# tests
print(loves_me(3))
print(loves_me(6))
print(loves_me(1))

