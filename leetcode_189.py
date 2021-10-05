# Rotate Array
class Solution:
    def rev(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return None

    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return None
        elif k >= len(nums):
            k = k % len(nums)
            self.rotate(nums, k)
        else:
            nums.reverse()
            self.rev(nums, 0, k-1)
            self.rev(nums, k, len(nums)-1)
        return None


s = Solution()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
s.rotate(nums, k=38)
print(nums)

nums = [1, 2]
s.rotate(nums, k=3)
print(nums)

nums = [1]
s.rotate(nums, k=0)
print(nums)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s.rotate(nums, k=3)
print(nums)

nums = [1]
s.rotate(nums, k=1)
print(nums)
