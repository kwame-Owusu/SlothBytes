"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

"""


def merge_alternately( word1: str, word2: str) -> str:
      result = ""
      i,j = 0,0
      # Merge the characters alternately
      while i < len(word1) and j < len(word2):
        result += word1[i] + word2[j]
        i += 1
        j += 1
      # Add the remaining characters from word1, if any
      while i < len(word1):
        result += word1[i]
        i += 1 
      # Add the remaining characters from word2, if any
      while j < len(word2):
        result += word2[j]
        j += 1
      
      return result



# Test cases
def test_merge_alternately():
    # Test case 1: Basic Test Case with Equal Length Strings
    assert merge_alternately("abc", "123") == "a1b2c3"
    
    # Test case 2: Basic Test Case with Different Length Strings
    assert merge_alternately("abcd", "12") == "a1b2cd"
    
    # Test case 3: Test Case with One Empty String
    assert merge_alternately("", "12345") == "12345"
    
    # Test case 4: Test Case with Both Empty Strings
    assert merge_alternately("", "") == ""
    
    # Test case 5: Test Case with Strings of Varying Lengths
    assert merge_alternately("abc", "123456789") == "a1b2c3456789"
    
    # Test case 7: Test Case with Mixed Case Letters
    assert merge_alternately("aB", "1c") == "a1Bc"
    
    print("All test cases pass.")

# Run the tests
test_merge_alternately()
