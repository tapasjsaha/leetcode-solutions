# Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        cnt = nums.count(target)
        if cnt == 0:
            return [-1, -1]
        else:
            left, right, lm = 0, len(nums), -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            lp = left
            return [lp, lp + cnt - 1]


s = Solution()
print(s.searchRange(nums=[1], target=1))

print(s.searchRange(nums=[1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 10], target=8))
print(s.searchRange(nums=[1, 2, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 10], target=2))
print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
print(s.searchRange(nums=[], target=0))

