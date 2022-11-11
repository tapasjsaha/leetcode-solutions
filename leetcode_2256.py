# Minimum Average Difference
class Solution:
    def minimumAverageDifference(self, nums: [int]) -> int:
        n = len(nums)
        for i in range(1, n, 1):
            nums[i] = nums[i] + nums[i-1]

        minad = 10**10
        res = 0

        for i in range(n):
            x = nums[i] // (i+1)
            y = (nums[n-1] - nums[i]) // (1 if (n - i -1) == 0 else (n - i - 1))
            if abs(x - y) < minad:
                minad = abs(x - y)
                res = i
        return res


s = Solution()
print(s.minimumAverageDifference(nums=[2, 5, 3, 9, 5, 3]))  # 3
print(s.minimumAverageDifference(nums=[0]))  # 0

