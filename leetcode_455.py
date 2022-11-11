# Assign Cookies
class Solution:
    def findContentChildren(self, g: [int], s: [int]) -> int:
        g.sort()
        s.sort()
        i, j, res = 0, 0, 0
        ni, nj = len(g), len(s)

        while i < ni and j < nj:
            if s[j] >= g[i]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1

        return res


s = Solution()
print(s.findContentChildren(g=[1, 2, 3], s=[1, 1]))
print(s.findContentChildren(g=[1, 2], s=[1, 2, 3]))
