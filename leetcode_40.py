# Combination Sum II
class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        res = []

        def backtrack(current, available):
            if sum(current) == target:
                res.append(current[:])
            elif sum(current) > target:
                return
            else:
                # construct candidates
                if not available:
                    return
                else:
                    key, val = available.popitem()
                    candidate_list = []
                    temp = []
                    while val >= 0:
                        candidate_list.append(temp[:])
                        temp.append(key)
                        val -= 1
                # Main loop
                    for candidate in candidate_list:
                        backtrack(current + candidate, available.copy())

        d = {}
        for candidate in sorted(candidates):
            if candidate in d:
                d[candidate] += 1
            else:
                d[candidate] = 1

        backtrack([], d.copy())
        return res


s = Solution()
print(s.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
print(s.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
print(s.combinationSum2(candidates=[1], target=1))
print(s.combinationSum2(candidates=[1], target=2))
print(s.combinationSum2(candidates=[2, 2, 2], target=5))

# res = []
#
#
# def backtrack(candidate_list, current_list):
#     if len(candidate_list) == 0:
#         pass
#     else:
#         (key, val) = candidate_list.popitem()
#         backtrack(candidate_list.copy(), current_list[:])
#         while val > 0:
#             current_list.append(key)
#             val -= 1
#             if sum(current_list) == target:
#                 res.append(current_list[:])
#             elif sum(current_list) > target:
#                 pass
#             else:
#                 backtrack(candidate_list.copy(), current_list[:])
#
#
# d = {}
# for candidate in candidates:
#     if candidate in d:
#         d[candidate] += 1
#     else:
#         d[candidate] = 1
#
# backtrack(d.copy(), [])
# return res