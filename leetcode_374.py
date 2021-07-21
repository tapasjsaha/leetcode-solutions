# Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
from time import sleep

class Solution:
    def guess(self, num):
        x = 1002     # Change pick
        if x < num:
            return -1
        elif x > num:
            return 1
        else:
            return 0

    def guessNumber(self, n):
        if self.guess(n) == 0:
            return n
        else:
            low = 1
            high = n
            while True:
                g = (low + high) // 2
                res = self.guess(g)
                if res == -1:
                    high = g
                elif res == 1:
                    low = g
                else:
                    return g

s = Solution()
print(s.guessNumber(2147483641))
