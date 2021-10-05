# House Robber
class Solution:
    def rob(self, nums: [int]) -> int:
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, ....]
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


s = Solution()
print(s.rob(nums=[2, 7, 9, 3, 1]))
print(s.rob(nums=[2, 7, 9, 3, 1, 5]))
