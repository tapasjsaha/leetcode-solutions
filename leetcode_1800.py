# Maximum Ascending Subarray Sum
class Solution:
    def maxAscendingSum(self, nums: [int]) -> int:
        i, maxvalue, currsum = 1, nums[0], nums[0]
        while i < len(nums):
            if nums[i] > nums[i-1]:
                currsum += nums[i]
                i += 1
            else:
                if currsum > maxvalue:
                    maxvalue = currsum
                currsum = nums[i]
                i += 1
        if currsum > maxvalue:
            return currsum
        else:
            return maxvalue


s = Solution()
print(s.maxAscendingSum(nums=[10, 20, 30, 5, 10, 50]))
print(s.maxAscendingSum(nums=[10, 20, 30, 40, 50]))
print(s.maxAscendingSum(nums=[12, 17, 15, 13, 10, 11, 12]))
print(s.maxAscendingSum(nums=[100, 10, 1]))
print(s.maxAscendingSum(nums=[10, 10, 10]))
print(s.maxAscendingSum(nums=[20]))
