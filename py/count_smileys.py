"""
Create a function that takes an array of strings and return the number of smiley faces contained within it. 
These are the components that make up a valid smiley:
    A smiley has eyes. Eyes can be : or ;
    A smiley has a nose but it doesn't have to. A nose can be - or ~
    A smiley has a mouth which can be ) or D 

No other characters are allowed except for those mentioned above.
"""
def count_smileys(arr: list[str]) -> int:
    valid_features = {
        "eyes": [":", ";"],
        "nose": ["-", "~"],
        "mouth": [")", "D"]
    }
    count = 0
    
    for face in arr:
       if (len(face) == 2 and face[0] in valid_features["eyes"] and face[1] in valid_features["mouth"]) or \
          (len(face) == 3 and face[0] in valid_features["eyes"] and face[1] in valid_features["nose"] and face[2] in valid_features["mouth"]):
          count += 1 
    return count


# Test cases
test1 = [":)", ";(", ";}", ":-D"]
test2 = [";D", ":-(", ":-)", ";~)"]
test3 = [";]", ":[", ";*", ":$", ";-D"]
print(count_smileys(test1))  #prints 2
print(count_smileys(test2))  #prints 3
print(count_smileys(test3))  #prints 1
