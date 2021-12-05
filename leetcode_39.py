# Combination Sum
class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        res = []

        def backtrack(current, remaining):
            if sum(current) == target:
                res.append(current[:])
            elif sum(current) > target:
                return
            else:
                # candidate_list = candidates
                for candidate in remaining:
                    indx = remaining.index(candidate)
                    backtrack(current+[candidate], remaining[indx:])

        backtrack([], candidates)
        return res


s = Solution()
print(s.combinationSum(candidates=[2, 3, 6, 7], target=7))
print(s.combinationSum(candidates=[2, 3, 6, 7], target=9))
print(s.combinationSum(candidates=[1], target=1))
print(s.combinationSum(candidates=[1], target=2))
print(s.combinationSum(candidates=[2], target=1))

res = []


# def backtrack(candidate_list, current_list):
#     if len(candidate_list) == 0:
#         pass
#     else:
#         current_list.append(candidate_list[0])
#         if sum(current_list) == target:
#             res.append(current_list[:])
#         elif sum(current_list) > target:
#             pass
#         else:
#             backtrack(candidate_list, current_list)
#         current_list.pop()
#         backtrack(candidate_list[1:], current_list)
#
#
# backtrack(candidates, [])