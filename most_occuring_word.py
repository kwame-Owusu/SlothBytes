"""Given an array of strings, return the words that is repeated the most"""

def most_occurring_word(words: list[str]) -> str:
    #Create an empty dictionary to store word counts
    word_count = {}

    #Count occurrences of each word in the list
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    #Find the word with the highest count
    max_count = 0
    most_occurred_word = None

    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            most_occurred_word = word

    return most_occurred_word


words = ["hello", "white", "black", "hello"]
print(most_occurring_word(words))
