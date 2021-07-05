#Power of Four
from math import log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0:
            x = log(n, 2)
            if x % 2 == 0:
                return True
            else:
                return False
        else:
            return False


s = Solution()
print(s.isPowerOfFour(n=0))
print(s.isPowerOfFour(n=1))
print(s.isPowerOfFour(n=4))
print(s.isPowerOfFour(n=16))
print(s.isPowerOfFour(n=5))
print(s.isPowerOfFour(n=-2147483648))

