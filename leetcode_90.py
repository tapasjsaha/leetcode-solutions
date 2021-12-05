# Subsets II
class Solution:
    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        res = []

        def backtrack(current, available):
            if not available:
                res.append(current[:])
            else:
                # create candidates
                candidate_list, temp = [], []
                key, val = available.popitem()
                while val >= 0:
                    val -= 1
                    candidate_list.append(temp[:])
                    temp.append(key)
                # print(candidate_list)
                # Main loop
                for candidate in candidate_list:
                    backtrack(current+candidate, available.copy())

        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        backtrack([], d.copy())
        return res


s = Solution()
print(s.subsetsWithDup(nums=[10, 20, 20]))

# res = []
# def findsubset(nums, n):
#     for i in range(2 ** n):
#         temp = []
#         for j in range(n):
#             if i & (1 << j) >= 1:
#                 temp.append(nums[j])
#         if temp not in res:
#             res.append(temp)
#
# nums.sort()
# n = len(nums)
# findsubset(nums, n)
# return list(res)