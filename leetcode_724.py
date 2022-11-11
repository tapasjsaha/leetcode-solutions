# Find Pivot Index
class Solution:
    def pivotIndex(self, nums: [int]) -> int:
        n = len(nums)
        for i in range(1, n, 1):
            nums[i] = nums[i] + nums[i-1]

        for i in range(n):
            pre = 0 if i == 0 else nums[i-1]
            post = nums[n-1] - nums[i]
            if pre == post:
                return i
        return -1



s = Solution()
print(s.pivotIndex(nums=[1, 7, 3, 6, 5, 6]))
print(s.pivotIndex(nums=[1, 2, 3]))
print(s.pivotIndex(nums=[2, 1, -1]))
