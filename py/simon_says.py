"""
Simon asks you to perform operations on a list of numbers that only he tells you.
You should ignore all other instructions given.
Create a function which evaluates a list of commands (written in plain English) if the command begins with Simon says. Return the result as an integer.
simon_says([
  "Simon says add 4",
  "Simon says add 6",
  "Then add 5"
])
output = 10

simon_says([
  "Susan says add 10",
  "Simon says add 3",
  "Simon says multiply by 8"
])
output = 24
"""

def simon_says(arr: list[str]) -> int:
   result = 0
   
   for command in arr:
      if command.startswith("Simon says"):
         operation = command[len("Simon says "):]
         
         if operation.startswith("add"): # Extract the number to add
            number = int(operation.split()[-1])
            result += number
         
         elif operation.startswith("subtract"): # Extract the number to subtract
            number = int(operation.split()[-1])
            result -= number
         
         elif operation.startswith("multiply"): # Extract the number to multiply
            number = int(operation.split()[-1])
            result *= number
   return result

    
# tests
print(simon_says(["Simon says add 4","Simon says add 6", "Then add 5"])) # 10
print(simon_says(["Susan says add 10","Simon says add 3","Simon says multiply by 8"])) # 24
print(simon_says([ "Firstly, add 4","Simeon says subtract 100"])) # 0
