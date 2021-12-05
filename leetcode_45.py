# Jump Game II
class Solution:
    def jump(self, nums: [int]) -> int:
        start = final = len(nums) - 1
        jumps_req = [10000] * len(nums)
        jumps_req[start] = 0
        while start > 0:
            start -= 1
            upper = min(final + 1, start + nums[start] + 1)
            jumps_req[start] = min((jumps_req[start:upper])) + 1
        print(nums)
        print(jumps_req)
        return jumps_req[0]


s = Solution()
print(s.jump(nums=[2, 3, 1, 1, 4]))
print(s.jump(nums=[2, 3, 0, 1, 4]))
print(s.jump(nums=[1, 1, 1, 1, 7]))
