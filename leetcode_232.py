# Implement Queue using Stacks
# Basically we need to implement a queue using two stacks, which means we cannot use pop(0) and can use only pop()
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.size > 0 and self.stack2:
            self.size -= 1
            return self.stack2.pop()
        elif self.size > 0 and not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.size -= 1
            return self.stack2.pop()
        else:
            return None

    def peek(self) -> int:
        if self.size > 0 and self.stack2:
            return self.stack2[-1]
        elif self.size > 0 and not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]
        else:
            return None

    def empty(self) -> bool:
        if self.size > 0:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())
