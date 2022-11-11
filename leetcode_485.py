# Max Consecutive Ones
class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        res = 0
        prev = nums[0]
        for curr in nums[1:]:
            res = max(res, prev + curr)
            prev = (prev + curr) if curr == 1 else 0
        return max(res, prev)


s = Solution()
print(s.findMaxConsecutiveOnes(nums=[1, 1, 0, 1, 1, 1]))
print(s.findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0, 1]))
