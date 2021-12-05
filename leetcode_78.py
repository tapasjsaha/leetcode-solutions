# Subsets
# Algo used SSS Backtracking
class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        res = []

        def backtracking(subset, n):
            if n == len(subset):
                temp = [nums[i] for i, s in enumerate(subset) if s]
                res.append(temp)
            else:
                candidate_list = [True, False]
                for candidate in candidate_list:
                    backtracking(subset + [candidate], n)

        n = len(nums)
        backtracking([], n)
        return res


s = Solution()
print(s.subsets(nums=[1, 2, 3]))


# def backtracking(start, subset):
#     if start >= len(nums):
#         res.append(subset[:])
#     else:
#         # Choice 1: with the element at start position
#         subset.append(nums[start])
#         backtracking(start + 1, subset)
#         # Choice 2: without the element at start position
#         subset.pop()
#         backtracking(start + 1, subset)
#
#
# backtracking(0, [])
# return res