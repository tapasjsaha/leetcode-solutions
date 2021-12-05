# Fibonacci Number
class Solution:
    # Iterative solution
    def fib(self, n: int) -> int:
        dp = [-1] * (n + 1)
        dp[0] = 0
        if len(dp) >= 2:
            dp[1] = 1

        for i in range(2, len(dp), 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# Recursion with memorization
# def fib(self, n: int) -> int:
#     cache = {0: 0, 1: 1}
#
#     def rec_fib(N):
#         if N in cache:
#             return cache[N]
#         else:
#             cache[N] = rec_fib(N - 1) + rec_fib(N - 2)
#             return cache[N]
#
#     return rec_fib(n)

s = Solution()
print(s.fib(n=0))
print(s.fib(n=1))
print(s.fib(n=2))
print(s.fib(n=5))
print(s.fib(n=50))
