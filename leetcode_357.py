# Count Numbers with Unique Digits
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            # for MSB - it can be 1-9, for next place 0-9 except already used and so forth
            ans = 9
            product = 1
            start =9
            for i in range(n-1):
                product = product * start
                start -= 1
            ans = ans * product
            return ans + self.countNumbersWithUniqueDigits(n-1)


s = Solution()
print(s.countNumbersWithUniqueDigits(n=2))
print(s.countNumbersWithUniqueDigits(n=0))
print(s.countNumbersWithUniqueDigits(n=8))
