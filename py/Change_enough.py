"""
Given a total due and an array representing the amount of change in your pocket, determine whether or not you are able to pay for the item. 

Change will always be represented in the following order: quarters, dimes, nickels, pennies.

Example: changeEnough([25, 20, 5, 0], 4.25) return true because:

25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50.

This means you can afford the item, so return true. 
"""

def change_enough(arr: list[int], due: float) -> bool:
  money: dict[str, float] = {
    "quarter" : 0.25,
    "dime" : 0.10,
    "nickel" : 0.05,
    "penny" : 0.01,
  }
  zipped = zip(money.values(), arr)
  res = 0
  for value, item in zipped:
    res += value * item
  
  if res < due:
    return False
  return True

        
#tests
print(change_enough([2, 100, 0, 0], 14.11)) # False
print(change_enough([0, 0, 20, 5], 0.75))# True
print(change_enough([30, 40, 20, 5], 12.55))# True
print(change_enough([10, 0, 0, 50], 3.85))# False
print(change_enough([1, 0, 5, 219], 19.99))# False
