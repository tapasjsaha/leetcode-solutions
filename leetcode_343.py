# Integer Break
# Hint - heck the breaking results of n ranging from 7 to 10 to discover the regularities
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0, 1, 2, 4, 6, 9]  # Created Manually
        if n <= 6:
            return dp[n-1]
        else:
            temp = 1
            while n > 6:
                temp *= 3
                n -= 3
            temp *= dp[n-1]
            return temp


s = Solution()
print(s.integerBreak(1))
print(s.integerBreak(6))
print(s.integerBreak(7))
print(s.integerBreak(12))
print(s.integerBreak(35))


