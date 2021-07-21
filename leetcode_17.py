# Letter Combinations of a Phone Number
class Solution:
    def letterCombinations(self, digits):
        letters = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']
                   }
        if digits:
            res = ['']
            out = []
            for d in digits:
                for ch in res:
                    for c in letters[d]:
                        out.append(ch + c)
                res = out.copy()
                out = []
        else:
            res = []
        return res


s = Solution()
print(s.letterCombinations(digits=""))
print(s.letterCombinations(digits="2"))
print(s.letterCombinations(digits="23"))
print(s.letterCombinations(digits="234"))