# Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: [int]) -> [int]:
        for i in range(1, len(nums), 1):
            nums[i] = nums[i] + nums[i-1]
        return nums


s = Solution()
print(s.runningSum(nums=[1, 2, 3, 4]))
print(s.runningSum(nums=[1, 1, 1, 1, 1]))
print(s.runningSum(nums=[3, 1, 2, 10, 1]))
