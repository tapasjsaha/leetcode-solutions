# Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        n = len(nums)
        curr = nums[0]
        j = 1
        for i in range(1, n):
            if nums[i] == curr:
                pass
            else:
                curr = nums[i]
                nums[j] = curr
                j += 1
        return j


s = Solution()
print(s.removeDuplicates(nums=[1, 1, 2]))
print(s.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
