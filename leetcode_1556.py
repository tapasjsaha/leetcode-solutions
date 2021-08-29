# Thousand Separator
class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = list(str(n))
        res = ''
        rem = 0
        while n:
            rem = n[-3:]
            n = n[:-3]
            if n:
                res = '.' + ''.join(rem) + res
        res = ''.join(rem) + res
        return res


s = Solution()
print(s.thousandSeparator(n=51040))
print(s.thousandSeparator(n=1000000))
print(s.thousandSeparator(n=987))
print(s.thousandSeparator(n=1234))
print(s.thousandSeparator(n=123456789))
print(s.thousandSeparator(n=0))

