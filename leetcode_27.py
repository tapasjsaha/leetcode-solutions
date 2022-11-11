# Remove Element
class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        n = len(nums)
        i, j = 0, n - 1
        while i < n and nums[i] != val:
            i += 1
        while j >= 0 and nums[j] == val:
            j -= 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            while i < n and nums[i] != val:
                i += 1
            while j >= 0 and nums[j] == val:
                j -= 1

        return i


s = Solution()
print(s.removeElement(nums=[3, 2, 2, 3], val=3))
print(s.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
