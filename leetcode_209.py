# Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: [int]) -> int:
        res = 100000  # nums.length <= 10**5
        if sum(nums) < target:  # nums is a list of positive integers (1 <= nums[i])
            return 0
        left, right, curr_sum = 0, 0, 0
        while right < len(nums):
            # print(nums[left:right + 1], res)
            curr_sum += nums[right]
            while curr_sum >= target:
                if curr_sum >= target:
                    res = min(res, (right - left + 1))
                curr_sum -= nums[left]
                left += 1
            right += 1
        return res


s = Solution()
print(s.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(target=4, nums=[1, 4, 4]))
print(s.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
print(s.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 11]))
print(s.minSubArrayLen(target=11, nums=[11, 1, 1, 1, 1, 1, 1, 1]))
print(s.minSubArrayLen(target=11, nums=[1, 1, 1, 11, 1, 1, 1, 1]))
