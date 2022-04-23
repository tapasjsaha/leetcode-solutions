# Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, sm = 1, 0
        while n:
            dig = n % 10
            n = n // 10
            prod *= dig
            sm += dig
        return prod - sm


s = Solution()
print(s.subtractProductAndSum(234))
print(s.subtractProductAndSum(4421))
print(s.subtractProductAndSum(1))
print(s.subtractProductAndSum(501))
