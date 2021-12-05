# Combinations
class Solution:
    def combine(self, n: int, k: int) -> [[int]]:
        res = []

        def backtrack(current, value):
            if len(current) == k:
                res.append(current[:])
            else:
                candidate_list = [a for a in range(value, n+1, 1)]
                for candidate in candidate_list:
                    value = candidate+1
                    backtrack(current+[candidate], value)

        backtrack([], 1)
        return res



s = Solution()
print(s.combine(4, 2))

# res = []
#
# def backtrack(start, comb):
#     if len(comb) == k:
#         res.append(comb[:])
#     else:
#         for i in range(start, n + 1, 1):
#             comb.append(i)
#             backtrack(i + 1, comb)
#             comb.pop()
#
#
# backtrack(1, [])
# return res