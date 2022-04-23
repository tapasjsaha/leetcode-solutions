class Solution:
    def isMonotonic(self, nums: [int]) -> bool:
        monotonic_increasing, monotonic_decreasing = True, True
        i = 1
        while i < len(nums) and (monotonic_increasing or monotonic_decreasing):
            if nums[i] < nums[i - 1]:
                monotonic_increasing = False
            if nums[i] > nums[i - 1]:
                monotonic_decreasing = False
            i += 1
        return monotonic_increasing or monotonic_decreasing


s = Solution()
print(s.isMonotonic(nums=[1, 2, 2, 3]))
print(s.isMonotonic(nums=[6, 5, 4, 4]))
print(s.isMonotonic(nums=[1, 3, 2]))
print(s.isMonotonic(nums=[1]))
