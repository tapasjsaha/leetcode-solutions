# Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        res = [1]*len(nums)
        current = 1
        # Multiply with product of prefix
        for i in range(len(nums)):
            res[i] *= current
            current *= nums[i]

        # Multiply with product of suffix
        current = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= current
            current *= nums[i]
        return res


s = Solution()
print(s.productExceptSelf(nums = [1,2,3,4]))
print(s.productExceptSelf(nums = [-1,1,0,-3,3]))
