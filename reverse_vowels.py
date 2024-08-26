"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"

"""
def reverseVowels(s: str) -> str:
      vowels = set("aeiouAEIOU")# Set of vowels for quick lookup
      s = list(s)# Convert string to list to allow modification

      left, right = 0, len(s) -1

      while left < right:
        #swap chars if they are in vowels else increment pointer by 1
        if s[left] in vowels and s[right] in vowels:
          s[left], s[right] = s[right], s[left]
          left += 1
          right -= 1
        if s[left] not in vowels:
          left += 1
        if s[right] not in vowels:
          right -= 1
      return "".join(s)# Convert list back to string


def test_reverseVowels():
    # Test case 1: Basic Test Case
    assert reverseVowels("hello") == "holle"
    
    # Test case 2: String with No Vowels
    assert reverseVowels("bcdf") == "bcdf"
    
    # Test case 3: All Vowels
    assert reverseVowels("aeiou") == "uoiea"
  
    # Test case 4: Mixed Case Vowels
    assert reverseVowels("aA") == "Aa"
    
    # Test case 5: Empty String
    assert reverseVowels("") == ""
    
    # Test case 6: Single Character String
    assert reverseVowels("e") == "e"
    
    # Test case 8: String with Only One Vowel
    assert reverseVowels("rhythm") == "rhythm"

    print("All test cases passed")

test_reverseVowels()
