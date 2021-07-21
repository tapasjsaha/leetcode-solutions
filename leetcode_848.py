# Shifting Letters
class Solution:
    def shiftingLetters(self, s, shifts):
        cnt = 0
        res = ''
        for i in range(len(s)-1, -1, -1):
            cnt += shifts[i]
            x = ord(s[i]) - 97 + cnt
            x %= 26
            res = chr(x + 97) + res
        return res


s = Solution()
print(s.shiftingLetters(s="abc", shifts=[3, 5, 9]))
print(s.shiftingLetters(s="abc", shifts=[1, 1, 1]))
print(s.shiftingLetters(s="a", shifts=[0]))
print(s.shiftingLetters(s="a", shifts=[10000000000]))