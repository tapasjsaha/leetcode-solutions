# Decode Ways
# https://www.youtube.com/watch?v=o1i7JYWbwOE
# Solution method same as house robber problem
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        deco1 = 0
        deco2 = 1
        prev = '0'
        # [doco1, deco2, 0, 1, 2 .... n]
        for ch in s:
            #print(deco1, deco2)
            res = 0
            if 1 <= int(ch) <= 9:
                res += deco2
            if 10 <= int(prev + ch) <= 26:
                res += deco1
            if res == 0:
                return 0
            else:
                deco1 = deco2
                deco2 = res
                prev = ch
        #print(deco1, deco2)
        return deco2




s = Solution()
print(s.numDecodings(s="0"))
print(s.numDecodings(s="12"))
print(s.numDecodings(s="226"))
print(s.numDecodings(s="06"))
print(s.numDecodings(s="10011"))
print(s.numDecodings(s="1101121"))
print(s.numDecodings(s="461012"))


