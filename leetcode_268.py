# Missing Number
class Solution:
    def missingNumber(self, nums: [int]) -> int:
        n = len(nums)
        trueSum = (n*(n+1))/2
        return int(trueSum - sum(nums))


s = Solution()
print(s.missingNumber(nums=[3, 0, 1]))
print(s.missingNumber(nums=[0, 1]))
print(s.missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(s.missingNumber(nums=[0]))
print(s.missingNumber(nums=[1, 2, 3]))
