# Permutations II
class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        res = []
        d = {}

        def backtrack(current, available):
            if len(current) == len(nums):
                res.append(current[:])
            else:
                candidate_list = [key for (key, val) in available.items() if val > 0]
                for candidate in candidate_list:
                    available[candidate] -= 1
                    backtrack(current + [candidate], available)
                    available[candidate] += 1

        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        backtrack([], d)
        return res


s = Solution()
print(s.permuteUnique(nums=[1, 1, 2]))

# res = []
# if len(nums) == 1:
#     return [nums[:]]
# else:
#     for i in range(len(nums)):
#         x = nums.pop(0)
#         pers = self.permuteUnique(nums)
#         for per in pers:
#             per.append(x)
#             if per not in res:
#                 res.append(per)
#         nums.append(x)
# return res