# Add Digits
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9


s = Solution()
print(s.addDigits(num=38))
print(s.addDigits(num=0))
print(s.addDigits(num=999999))
print(s.addDigits(num=1198))
