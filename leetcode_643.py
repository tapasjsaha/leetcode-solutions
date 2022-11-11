# Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: [int], k: int) -> float:
        total = 0
        for i in range(k):
            total += nums[i]
        avg = total / k
        for i in range(k, len(nums), 1):
            total = total - nums[i - k] + nums[i]
            avg = max(avg, total / k)
        return avg


s = Solution()
print(s.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
print(s.findMaxAverage(nums=[5], k=1))
