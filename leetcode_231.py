# Power of Two

# n = 2^x
# log(n, 2) = x * log(2, 2)  => x = log(n, 2) as log(2, 2) = 1
from math import log


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        else:
            x = round(log(n, 2), 12)
            return x.is_integer()


s1 = Solution()

print(s1.isPowerOfTwo(-4))
print(s1.isPowerOfTwo(0))
print(s1.isPowerOfTwo(1))
print(s1.isPowerOfTwo(16))
print(s1.isPowerOfTwo(3))
print(s1.isPowerOfTwo(536870912))
print(s1.isPowerOfTwo(2147483648))
print(s1.isPowerOfTwo(2147483647))
