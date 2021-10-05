# Search Insert Position
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        low, mid, high = 0, 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return mid if nums[mid] > target else (mid+1)


s = Solution()
print(s.searchInsert(nums=[1, 3, 5, 6], target=5))
print(s.searchInsert(nums=[1, 3, 5, 6], target=2))
print(s.searchInsert(nums=[1, 3, 5, 6], target=7))
print(s.searchInsert(nums=[1, 3, 5, 6], target=0))
print(s.searchInsert(nums=[1], target=0))

print(s.searchInsert(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(s.searchInsert(nums=[-1, 0, 3, 5, 9, 12], target=2))
