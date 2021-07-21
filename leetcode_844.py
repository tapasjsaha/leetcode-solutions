# Backspace String Compare
class Solution:
    def backspaceCompare(self, s, t):
        ls, lt = [], []
        for ch in s:
            if ch != '#':
                ls.append(ch)
            else:
                try:
                    ls.pop()
                except IndexError:
                    pass
        for ch in t:
            if ch != '#':
                lt.append(ch)
            else:
                try:
                    lt.pop()
                except IndexError:
                    pass
        return ls == lt


s = Solution()
print(s.backspaceCompare(s="ab#c", t="ad#c"))
print(s.backspaceCompare(s="ab##", t="c#d#"))
print(s.backspaceCompare(s="a##c", t="#a#c"))
print(s.backspaceCompare(s="a#c", t="b"))
