"""Given an array of strings, return the words that is repeated the most"""

def most_occurring_word(words: list[str]) -> str:
    # Create an empty dictionary to store word counts
    word_count = {}

    # Count occurrences of each word in the list
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Find the word with the highest count
    max_count = 0
    most_occurred_word = None

    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            most_occurred_word = word

    return most_occurred_word

# Test cases using assert
words1 = ["hello", "white", "black", "hello"]
words2 = ["dog", "cat", "dog", "bird", "cat", "cat"]
words3 = ["apple", "banana", "apple", "apple", "banana", "orange"]
words4 = ["single", "single", "single"]
words5 = ["unique", "words", "here"]
words6 = ["tie", "tie", "breaker", "breaker"]

assert most_occurring_word(words1) == "hello", "Test case 1 failed"
assert most_occurring_word(words2) == "cat", "Test case 2 failed"
assert most_occurring_word(words3) == "apple", "Test case 3 failed"
assert most_occurring_word(words4) == "single", "Test case 4 failed"
assert most_occurring_word(words5) == "unique", "Test case 5 failed"
assert most_occurring_word(words6) in ["tie", "breaker"], "Test case 6 failed"  # Both "tie" and "breaker" are valid

print("All test cases passed!")
