# Binary Number with Alternating Bits
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n & 1
        n = n >> 1
        while n != 0:
            curr = n & 1
            n = n >> 1
            if curr != prev ^ 1:
                return False
            else:
                prev = curr
        return True


s = Solution()
print(s.hasAlternatingBits(n=5))
print(s.hasAlternatingBits(n=7))
print(s.hasAlternatingBits(n=11))
print(s.hasAlternatingBits(n=1))
