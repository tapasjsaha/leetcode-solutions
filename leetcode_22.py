# Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        res = []

        def backtrack(current, start, end):
            if start == 0 and end == 0:
                res.append(''.join(current[:]))
            elif start < 0 or end < 0 or start > end:
                return
            else:
                candidate_list = ['(', ')']
                for candidate in candidate_list:
                    backtrack(current + [candidate], start-1 if candidate == '(' else start, end-1 if candidate == ')' else end)

        backtrack([], n, n)
        return res


s = Solution()
print(s.generateParenthesis(3))
#print(s.generateParenthesis(4))

# res = []
#
# def backtrack(start, end, current):
#     if start == 0 and end == 0:
#         res.append(current)
#     elif start < end:
#         if start > 0:
#             backtrack(start - 1, end, current + "(")
#             backtrack(start, end - 1, current + ")")
#         else:
#             backtrack(start, end - 1, current + ")")
#     else:
#         backtrack(start - 1, end, current + "(")
#
# backtrack(n, n, "")
# return res