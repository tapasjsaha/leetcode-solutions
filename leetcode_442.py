# Find All Duplicates in an Array
class Solution:
    def findDuplicates(self, nums):
        res = []
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                res.append(n)
        return res


s = Solution()
print(s.findDuplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
print(s.findDuplicates(nums=[1, 1, 2]))
print(s.findDuplicates(nums=[1]))
print(s.findDuplicates(nums=[1, 2]))
