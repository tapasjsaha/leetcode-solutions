# Find Peak Element
class Solution:
    def findPeakElement(self, nums: [int]) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] >= nums[mid+1]:
                high = mid
            else:
                low = mid + 1
        return low


s = Solution()
print(s.findPeakElement(nums=[1, 2, 3, 1]))
print(s.findPeakElement(nums=[1, 2, 1, 3, 5, 6, 4]))
