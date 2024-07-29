"""A function that accepts a phrase and returns the number of vowels present
    Args:
        phrase (str): The user input string to determine the number of vowels
    Returns:
        int: the number of vowels present in user input string
"""
def has_vowels(word: str) -> int:
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count

# Test cases
assert has_vowels("hello world") == 3, "Test case 1 failed"
assert has_vowels("stray cats") == 2, "Test case 2 failed"
assert has_vowels("programmer") == 3, "Test case 3 failed"
assert has_vowels("") == 0, "Test case 4 failed"
assert has_vowels("rhythm") == 0, "Test case 5 failed"
assert has_vowels("aeiou") == 5, "Test case 6 failed"
assert has_vowels("AEIOU") == 5, "Test case 7 failed"
assert has_vowels("HeLLo WoRLD") == 3, "Test case 8 failed"

print("All test cases passed!")
