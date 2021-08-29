# Rearrange Spaces Between Words
class Solution:
    def reorderSpaces(self, text: str) -> str:
        ns = text.count(' ')
        lsw = text.split()
        sc = len(lsw) - 1
        if sc != 0:
            pad = ' ' * (ns // sc)
            end = ' ' * (ns % sc)
        else:
            pad = ''
            end = ' ' * ns
        res = pad.join(lsw)
        res += end
        # return '"'+res+'"'
        return res


s = Solution()
print(s.reorderSpaces(text = "  this   is  a sentence "))
print(s.reorderSpaces(text = " practice   makes   perfect"))
print(s.reorderSpaces(text = "hello   world"))
print(s.reorderSpaces(text = "  walks  udp package   into  bar a"))
print(s.reorderSpaces(text = "a"))
print(s.reorderSpaces(text = "     a"))