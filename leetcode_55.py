# Jump Game
class Solution:
    def canJump(self, nums: [int]) -> bool:
        start = final = len(nums) - 1
        while start > 0:
            if start + nums[start] >= final:
                final = start
            start -= 1
        return start + nums[start] >= final


s = Solution()
print(s.canJump(nums=[2, 3, 1, 1, 4]))
print(s.canJump(nums=[3, 2, 1, 0, 4]))
print(s.canJump(nums=[0]))

