# Pow(x, n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return self.myPow(1 / x, -n)
        elif n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x, n - 1)


s = Solution()
print(s.myPow(x=2.00000, n=10))
print(s.myPow(x=2.10000, n=3))
print(s.myPow(x=2.00000, n=-2))
print(s.myPow(x=2.00000, n=0))
print(s.myPow(x=0, n=0))
