# Search in Rotated Sorted Array
class Solution:
    def search(self, nums: [int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            # print(low, mid, high, nums[low:high + 1])
            if nums[mid] == target:
                return mid
            elif nums[low] < nums[mid] and nums[low] <= target < nums[mid]:
                high = mid - 1
            elif nums[mid] < nums[high] and nums[mid] < target <= nums[high]:
                low = mid + 1
            elif nums[low] <= nums[mid] and not nums[low] <= target < nums[mid]:
                low = mid + 1
            elif nums[mid] <= nums[high] and not nums[mid] < target <= nums[high]:
                high = mid - 1
        return -1


s = Solution()
print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=5))
print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
print(s.search(nums=[1], target=0))
print(s.search(nums=[3, 1], target=1))
