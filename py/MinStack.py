
"""
Design a Stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.

    void push(int val) pushes the element val onto the stack.

    void pop() removes the element on the top of the stack.

    int top() gets the top element of the stack.

    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Notes: the solution is to create a another stack that will keep track of the minimum element.
"""

class MinStack:
    def __init__(self) -> None:
      self.stack = []
      self.min_stack = []
    
    def push(self, val: int) -> None:
       self.stack.append(val)
       if not self.min_stack or val <=self.min_stack[-1]:
          self.min_stack.append(val)
    
    def pop(self) -> None:
      if self.stack.pop() == self.min_stack[-1]:
        self.min_stack.pop()
    
    def top(self) -> int:
       return self.stack[-1]
    
    def get_min(self) -> int:
       return self.min_stack[-1]
    
      
          
#test
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.get_min()) # return -3
min_stack.pop()
print(min_stack.top()) # returns 0
print(min_stack.get_min()) #returns -2

