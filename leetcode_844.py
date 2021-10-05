# Backspace String Compare
class Solution:
    def backspaceCompare(self, s, t):
        def getString(st):
            lst = []
            for ch in st:
                if ch != '#':
                    lst.append(ch)
                else:
                    try:
                        lst.pop()
                    except IndexError:
                        pass
            return lst

        return getString(s) == getString(t)


s = Solution()
print(s.backspaceCompare(s="ab#c", t="ad#c"))
print(s.backspaceCompare(s="ab##", t="c#d#"))
print(s.backspaceCompare(s="a##c", t="#a#c"))
print(s.backspaceCompare(s="a#c", t="b"))
