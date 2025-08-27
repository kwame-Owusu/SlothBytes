"""
Given a letter, created a function which returns the nearest vowel to the letter.
 If two vowels are equal distance to the given letter, return the earlier vowel.

 Notes:
    -All letters will be given in lowercase.
    -There will be no alphabet wrapping involved, meaning the closest vowel to "z" should return "u", not "a".
"""
def nearest_vowel(letter: str) -> str:
    letter = letter.lower()
    vowels = ["a", "e", "i", "o", "u"]
    min_distance = float('inf')
    nearest_vowel = ""
    for vowel in vowels:
        # Calculate the absolute distance between the letter and the vowel
        distance = abs(ord(letter) - ord(vowel))

        if distance < min_distance:
            min_distance = distance
            nearest_vowel = vowel
    return nearest_vowel

#tests
print(nearest_vowel("z")) #output = u
print(nearest_vowel("c")) #output = a
print(nearest_vowel("i")) #output = i
