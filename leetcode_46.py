# Permutations
class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        res = []

        def backtrack(current, remaining):
            if not remaining:
                res.append(current[:])
            else:
                candidate_list = [r for r in remaining]
                for candidate in candidate_list:
                    remaining.remove(candidate)
                    backtrack(current+[candidate], remaining)
                    remaining.append(candidate)

        backtrack([], nums[:])
        return res


s = Solution()
print(s.permute([1, 2, 3, 4]))


# def permute(self, nums: [int]) -> [[int]]:
#     res = []
#     if len(nums) == 1:
#         return [nums[:]]
#     else:
#         for i in range(len(nums)):
#             x = nums.pop(0)
#             perms = self.permute(nums)
#             for perm in perms:
#                 perm.append(x)
#             res.extend(perms)
#             nums.append(x)
#     return res