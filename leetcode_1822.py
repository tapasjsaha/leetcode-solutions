# Sign of the Product of an Array
class Solution:
    def arraySign(self, nums: [int]) -> int:
        res = 1
        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                res *= -1
            # No need for any operation on positive number as it does not impact the result
        return res


s = Solution()
print(s.arraySign(nums=[-1, -2, -3, -4, 3, 2, 1]))
print(s.arraySign(nums=[1, 5, 0, 2, -3]))
print(s.arraySign(nums=[-1, 1, -1, 1, -1]))
