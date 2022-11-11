# Count Good Numbers
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # for any even position possible digits are -> 0,2,4,6,8 i.e. total 5
        # for any odd position possible digits are -> 2,3,5,7 i.e. total 4
        from sys import setrecursionlimit
        setrecursionlimit(10 ** 5)

        def power(x, y, m):
            if y == 0:
                return 1
            p = power(x, y // 2, m)
            if y & 1 == 0:
                return (p * p) % m
            else:
                return (x * p * p) % m

        m = 10 ** 9 + 7
        p = n // 2
        ans = power(20, p, m)
        if n % 2 == 1:
            return (5 * ans) % m
        else:
            return ans


s = Solution()
print(s.countGoodNumbers(n=1))
print(s.countGoodNumbers(n=4))
print(s.countGoodNumbers(n=50))
