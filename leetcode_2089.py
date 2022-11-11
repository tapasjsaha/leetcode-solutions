# Find Target Indices After Sorting Array
class Solution:
    def targetIndices(self, nums: [int], target: int) -> [int]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res


s = Solution()
print(s.targetIndices(nums=[1, 2, 5, 2, 3], target=2))
print(s.targetIndices(nums=[1, 2, 5, 2, 3], target=3))
print(s.targetIndices(nums=[1, 2, 5, 2, 3], target=5))
