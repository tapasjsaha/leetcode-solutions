# Move Zeroes
class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums)
        while i < j:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                j -= 1
            else:
                i += 1
        #return None
        return nums


s = Solution()
print(s.moveZeroes(nums=[0, 1, 0, 3, 12]))
print(s.moveZeroes(nums=[0]))
print(s.moveZeroes(nums=[0, 1, 0, 0, 12, 0, 0]))
