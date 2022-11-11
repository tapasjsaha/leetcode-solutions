# XOR Operation in an Array
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            num = start + 2 * i
            res = res ^ num
        return res


s = Solution()
print(s.xorOperation(n=5, start=0))
print(s.xorOperation(n=4, start=3))
