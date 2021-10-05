# Binary Search
class Solution:
    def search(self, nums: [int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1


s = Solution()
print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
