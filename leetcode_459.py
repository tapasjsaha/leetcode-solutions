# Repeated Substring Pattern
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ls = len(s)
        r = 1
        while r <= ls//2:
            part = s[:r]
            lpart = len(part)
            if part * (ls//lpart) == s:
                return True
            r += 1
        return False


s = Solution()
print(s.repeatedSubstringPattern(s='abab'))
print(s.repeatedSubstringPattern(s='aba'))
print(s.repeatedSubstringPattern(s='abcabcabcabc'))
print(s.repeatedSubstringPattern(s='a'))
print(s.repeatedSubstringPattern(s='aa'))
print(s.repeatedSubstringPattern(s='ab'))