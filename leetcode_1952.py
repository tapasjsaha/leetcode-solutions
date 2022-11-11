# Three Divisors
class Solution:
    def isThree(self, n: int) -> bool:
        cnt = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                if n // i == i:
                    cnt += 1
                else:
                    cnt += 2
            i += 1
        return cnt == 3


s = Solution()
print(s.isThree(n=2))
print(s.isThree(n=4))
