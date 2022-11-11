# Build Array from Permutation
# Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?
# => make num = len(num) * [nums[nums[i]] + nums[i]
# hence new value will be num // len(num)
# old value will be num % len(num)
# this is how we can preserve both old and new value

class Solution:
    def buildArray(self, nums: [int]) -> [int]:
        n = len(nums)
        for i in range(n):
            nums[i] = n * (nums[nums[i]] % n) + nums[i]

        return [x//n for x in nums]


s = Solution()
print(s.buildArray(nums=[0, 2, 1, 5, 3, 4]))
print(s.buildArray(nums=[5, 0, 1, 2, 3, 4]))


# # S.C - O(N)
# class Solution:
#     def buildArray(self, nums: [int]) -> [int]:
#         res = [nums[n] for n in nums]
#         return res
#
#
# s = Solution()
# print(s.buildArray(nums=[0, 2, 1, 5, 3, 4]))
# print(s.buildArray(nums=[5, 0, 1, 2, 3, 4]))
