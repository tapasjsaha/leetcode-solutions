# Water Bottles
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        curr = numBottles
        while curr >= numExchange:
            new = curr // numExchange
            extra = curr % numExchange
            total += new
            curr = new + extra
        return total


s1 = Solution()

print(s1.numWaterBottles(numBottles=9, numExchange=3))
print(s1.numWaterBottles(numBottles=15, numExchange=4))
print(s1.numWaterBottles(numBottles=5, numExchange=5))
print(s1.numWaterBottles(numBottles=2, numExchange=3))
