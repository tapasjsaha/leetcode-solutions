# Binary Gap
class Solution:
    def binaryGap(self, n: int) -> int:
        if n & (n - 1) == 0:
            return 0
        else:
            res = 0
            cnt = -1
            while n:
                if n & 1 == 1 and cnt == -1:
                    cnt = 1
                elif n & 1 == 1:
                    res = max(res, cnt)
                    cnt = 1
                elif n & 1 == 0 and cnt != -1:
                    cnt += 1
                n = n >> 1
            return res


s = Solution()
print(s.binaryGap(n=22))
print(s.binaryGap(n=8))
print(s.binaryGap(n=5))
