# Minimum Value to Get Positive Step by Step Sum
class Solution:
    def minStartValue(self, nums: [int]) -> int:
        res = 0
        curr = 0
        for n in nums:
            curr += n
            res = min(res, curr)
        if res < 0:
            return 1 - res
        else:
            return 1


s = Solution()
print(s.minStartValue(nums=[-3, 2, -3, 4, 2]))
print(s.minStartValue(nums=[1, 2]))
print(s.minStartValue(nums=[1, -2, -3]))
