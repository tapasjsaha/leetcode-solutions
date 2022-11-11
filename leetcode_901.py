# Online Stock Span
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        day = 1
        if not self.stack:
            self.stack.append([price, day])
        else:
            while self.stack and self.stack[-1][0] <= price:
                prev = self.stack.pop()
                day += prev[1]
            self.stack.append([price, day])
        return day


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

obj = StockSpanner()
print(obj.next(price=100))
print(obj.next(price=80))
print(obj.next(price=60))
print(obj.next(price=70))
print(obj.next(price=60))
print(obj.next(price=75))
print(obj.next(price=85))

# Output : null, 1, 1, 1, 2, 1, 4, 6
