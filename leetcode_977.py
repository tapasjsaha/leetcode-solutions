# Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: [int]) -> [int]:
        i, j = 0, len(nums) - 1
        res = []
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                res.insert(0, nums[i] * nums[i])
                i += 1
            else:
                res.insert(0, nums[j] * nums[j])
                j -= 1
        return res


s = Solution()
print(s.sortedSquares(nums=[-4, -1, 0, 3, 10]))
print(s.sortedSquares(nums=[-7, -3, 2, 3, 11]))
