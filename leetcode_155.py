# Min Stack
class MinStack:
    def __init__(self):
        self.stack = []
        #self.min_so_far = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            min_so_far = min(float('inf'), val)
        else:
            min_so_far = min(self.stack[-1][1], val)
        self.stack.append((val, min_so_far))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        #v, m = self.stack[-1]
        return self.stack[-1][0]

    def getMin(self) -> int:
        #v, m = self.stack[-1]
        return self.stack[-1][1]


# Test case 3
obj = MinStack()
obj.push(-10)
obj.push(14)
print(obj.getMin()) #-10
print(obj.getMin()) #-10
obj.push(-20)
print(obj.getMin()) #-20
print(obj.getMin()) #-20
print(obj.top()) #-20
print(obj.getMin()) #-20
obj.pop()
obj.push(-10)
obj.push(-7)
print(obj.getMin()) #-10
obj.push(-7)
obj.pop()
print(obj.top()) #-7
print(obj.getMin()) #-10
obj.pop()

# Test case 2
obj = MinStack()
obj.push(2147483646)
obj.push(2147483646)
obj.push(2147483647)
print(obj.top())   # 2147483647
obj.pop()
print(obj.getMin()) # 2147483646
obj.pop()
print(obj.getMin()) # 2147483646
obj.pop()
obj.push(2147483647)
print(obj.top()) # 2147483647
print(obj.getMin()) # 2147483647
obj.push(-2147483648)
print(obj.top()) # -2147483648
print(obj.getMin()) #-2147483648
obj.pop()
print(obj.getMin()) #2147483647

# Test case 1
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())