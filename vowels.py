"""A function that accepts a phrase and returns the number of vowels present

    Args:
        phrase (str): The user input string to determine the number of vowels

    Returns:
        int: the number of vowels present in user input string
"""

def has_vowels(word: str) -> int:
    vowels = ("a", "e","o", "u")
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count

test1 = "hello world"
test2 = "stray cats"
test3 = "programmer"
print(f"{test1} has {has_vowels(test1)} vowels")
print(f"{test2} has {has_vowels(test2)} vowels")
print(f"{test3} has {has_vowels(test3)} vowels")