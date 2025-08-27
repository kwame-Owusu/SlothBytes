"""
Create a function that finds the first non-repeating character in a string and returns its index. If there is no non-repeating character, return -1.
Examples:

"leetcode" → 0 (because 'l' is the first character that only appears once)
"loveleetcode" → 2 (because 'v' is the first character that only appears once)
"aabb" → -1 (because every character appears twice)
"aaa" → -1 (because 'a' appears three times)

"""

def find_non_repeating(word: str) -> int:
    char_info = {}
    
    # Store count and position in one pass
    for i, char in enumerate(word):
        if char not in char_info:
            char_info[char] = {"count": 1, "first_pos": i}
        else:
            char_info[char]["count"] += 1
    
    # Find earliest position of any non-repeating character
    min_index = float('inf')
    for char_data in char_info.values():
        if char_data["count"] == 1:
            min_index = min(min_index, char_data["first_pos"])
    
    # Return -1 if no non-repeating character found
    return min_index if min_index != float('inf') else -1

print(find_nonrepeating("lleetcode"))
