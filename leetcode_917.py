#Reverse Only Letters
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        t = list(s)
        i = 0
        j = len(t) - 1
        while i < j:
            if ord(t[i].lower()) < 97 or ord(t[i].lower()) > 122:
                i += 1
            elif ord(t[j].lower()) < 97 or ord(t[j].lower()) > 122:
                j -= 1
            else:
                t[i], t[j] = t[j], t[i]
                i += 1
                j -= 1
        s = ''.join(t)
        return s


s = Solution()
print(s.reverseOnlyLetters(s = 'a-bcd'))
print(s.reverseOnlyLetters(s = 'xy--z'))