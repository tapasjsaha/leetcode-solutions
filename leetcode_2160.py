# Minimum Sum of Four Digit Number After Splitting Digits
class Solution:
    def minimumSum(self, num: int) -> int:
        l = list(str(num))
        l.sort()
        new1 = l[0] + l[2]
        new2 = l[1] + l[3]
        return int(new1) + int(new2)


s = Solution()
print(s.minimumSum(num=2932))
print(s.minimumSum(num=4009))
