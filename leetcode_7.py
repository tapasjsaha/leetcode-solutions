# Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        mf = -1 if x < 0 else 1
        num = -1 * x if x < 0 else x
        x = 0
        while num != 0:
            rem = num % 10
            x = (x * 10) + rem
            num = num // 10
        x *= mf
        if x.bit_length() < 32:
            return x
        else:
            return 0


s = Solution()
print(s.reverse(x=123))
print(s.reverse(x=-123))
print(s.reverse(x=-120))
print(s.reverse(x=0))
print(s.reverse(x=2147483648))
