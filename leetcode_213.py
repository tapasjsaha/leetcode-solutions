# House Robber II
class Solution:
    def rob(self, nums: [int]) -> int:
        def valueFromRob(values):
            rob1, rob2 = 0, 0
            # [rob1, rob2, n, n+1, ....]
            for value in values:
                temp = max(value + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        if len(nums) == 1:
            return nums[0]
        else:
            return max(valueFromRob(nums[:-1]), valueFromRob(nums[1:]))


s = Solution()
print(s.rob(nums=[2, 3, 2]))
print(s.rob(nums=[1, 2, 3, 1]))
print(s.rob(nums=[3, 2]))
print(s.rob(nums=[5]))

