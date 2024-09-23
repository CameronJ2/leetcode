class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min or self.min[-1] > val:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])
        

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


obj = MinStack()

obj.push(5)
obj.push(9)
obj.push(10)
obj.push(11)
obj.push(4)

print(obj.getMin())