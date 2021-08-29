# Sum of Absolute Differences in a Sorted Array
class Solution:
    def getSumAbsoluteDifferences(self, nums: [int]) -> [int]:
        totalSum, runningSum, numElement = sum(nums), 0, len(nums)
        res = []
        for i, x in enumerate(nums):
            res.append(x*i - runningSum - (x*(numElement-i) - totalSum))
            runningSum += x
            totalSum -= x
        return res


s = Solution()
print(s.getSumAbsoluteDifferences(nums=[2, 3, 5]))
print(s.getSumAbsoluteDifferences(nums=[1, 4, 6, 8, 10]))
