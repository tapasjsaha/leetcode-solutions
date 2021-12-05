# Letter Case Permutation
class Solution:
    def letterCasePermutation(self, s: str) -> [str]:
        res = []

        def backtrack(current, available):
            if not available:
                res.append(''.join(current))
            else:
                if available[0].isalpha():
                    candidate_list = [available[0].upper(), available[0].lower()]
                else:
                    candidate_list = [available[0]]
                for candidate in candidate_list:
                    backtrack(current+[candidate], available[1:])

        backtrack([], s)
        return res


s = Solution()
print(s.letterCasePermutation(s="1"))
print(s.letterCasePermutation(s="a"))
print(s.letterCasePermutation(s="12"))
print(s.letterCasePermutation(s="a1"))
print(s.letterCasePermutation(s="a1b2"))


# def letterCasePermutation(self, s: str) -> [str]:
#     res = []
#     if len(s) == 1:
#         if not s.isalpha():
#             return [str(s)]
#         else:
#             return [s.upper(), s.lower()]
#     else:
#         ch = []
#         if s[0].isdigit():
#             ch.append(str(s[0]))
#         else:
#             ch.append(s[0].lower())
#             ch.append(s[0].upper())
#         st = s[1:]
#         vals = self.letterCasePermutation(st)
#         for c in ch:
#             res.extend([c + str(val) for val in vals])
#     return res
