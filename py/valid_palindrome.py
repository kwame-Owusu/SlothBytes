"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
 it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

def is_palindrome(word: str) -> bool:
    filtered_word = "".join(char.lower() for char in word if char.isalnum())
    left = 0
    right = len(filtered_word) -1
    while left < right:
        if filtered_word[left] != filtered_word[right]:
            return False
        left +=1
        right -=1
    return True


#test cases
s = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = "Able , was I saw eLba"
s4 = "No 'x' in Nixon"
s5 = "123abccba321"
print(is_palindrome(s))
print(is_palindrome(s2))
print(is_palindrome(s3))
print(is_palindrome(s4))
print(is_palindrome(s5))
