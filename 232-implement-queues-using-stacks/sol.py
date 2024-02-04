# Implement a first in first out (FIFO) queue using only two stacks. 
# The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

class MyQueue:
    
    def __init__(self):
        self.stackOne = []
        self.stackTwo = []
        

    def push(self, x: int) -> None:
        while self.stackOne:
            self.stackTwo.append(self.stackOne.pop())
            
        self.stackTwo.append(x)
        
        while self.stackTwo:
            self.stackOne.append(self.stackTwo.pop())
            

    def pop(self) -> int:
        return self.stackOne.pop()
        

    def peek(self) -> int:
        return self.stackOne[-1]
        

    def empty(self) -> bool:
        return not self.stackOne

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()