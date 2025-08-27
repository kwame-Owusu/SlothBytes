"""Check if a string is formatted as a title. A title string is when every word of the string start with a upper case letter."""

def check_Title(word: str) -> bool:
    words = word.split(" ")
    for w in words:
        if w != w.capitalize():
            return False
    return True


print(check_Title("A Mind Boggling Achievement"))
print(check_Title("A Simple C++ Program!"))
print(check_Title("Water is transparent"))