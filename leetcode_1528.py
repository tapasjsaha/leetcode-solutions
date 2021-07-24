# Shuffle String
class Solution:
    def restoreString(self, s: str, indices: [int]) -> str:
        res = [''] * len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(res)


s = Solution()
print(s.restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]))
print(s.restoreString(s="abc", indices=[0, 1, 2]))
print(s.restoreString(s="aiohn", indices=[3, 1, 4, 2, 0]))
print(s.restoreString(s="aaiougrt", indices=[4, 0, 2, 6, 7, 3, 1, 5]))
print(s.restoreString(s="art", indices=[1, 0, 2]))
