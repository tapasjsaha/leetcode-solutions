# Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: [int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            # print(nums[low:high+1])
            if nums[low] <= nums[high]:  # list is already sorted
                return nums[low]
            elif nums[low] <= nums[mid] and nums[high] < nums[mid]:
                low = mid + 1
            elif nums[low] > nums[mid] and nums[high] > nums[mid]:
                high = mid


s = Solution()
print(s.findMin(nums=[0, 1, 2, 4, 5, 6, 7]))
print(s.findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
print(s.findMin(nums=[4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2]))
print(s.findMin(nums=[60, 70, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

print(s.findMin(nums=[3, 4, 5, 1, 2]))
print(s.findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
print(s.findMin(nums=[11, 13, 15, 17]))
print(s.findMin(nums=[3]))
print(s.findMin(nums=[3, 1]))
