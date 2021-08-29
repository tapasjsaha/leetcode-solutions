# Sum of Digits in Base K
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n:
            res += n % k
            n = n // k
        return res


s = Solution()
print(s.sumBase(n=34, k=6))
print(s.sumBase(n=10, k=10))
