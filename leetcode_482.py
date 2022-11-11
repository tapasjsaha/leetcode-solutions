# License Key Formatting
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        n = len(s)
        r = 0
        res = ''
        for i in range(n-1,-1,-1):
            if r == k:
                res = '-'+res
                r = 0
            if s[i] != '-':
                res = s[i].upper() + res
                r += 1
        if res == '':
            return res
        elif res[0] == '-':
            return res[1:]
        else:
            return res


s = Solution()
print(s.licenseKeyFormatting(s="5F3Z-2e-9-w", k=4))
print(s.licenseKeyFormatting(s="2-5g-3-J", k=4))
