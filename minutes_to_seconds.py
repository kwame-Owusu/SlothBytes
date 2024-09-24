"""
You are given the length of a video in minutes. The format is mm:ss (ex: "02:54").
Create a function that takes the video length and return it in seconds.
examples:
minutesToSeconds("01:00") = 60
minutesToSeconds("10:60") = -1
minuteToSeconds("121:49") = 7309

Notes:
    The video length is given as a string.
    If the number of seconds is 60 or over, return -1 (see example #3).
    You may get a number of minutes over 99 (e.g. "121:49" is perfectly valid).

"""

def minutes_to_seconds(mins_to_secs: str) -> int:
    parts = mins_to_secs.split(":")
    mins = int(parts[0])
    secs = int(parts[1])
    if secs >= 60:
        return -1
    return mins * 60 + secs


#test cases
print(minutes_to_seconds('01:00'))#60
print(minutes_to_seconds('13:56'))#836
print(minutes_to_seconds('10:60'))#-1
print(minutes_to_seconds('121:49'))#7309
    
