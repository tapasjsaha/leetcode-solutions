# String Without AAA or BBB
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = ''
        if a < b:
            more, less = 'b', 'a'
            mn, ln = b, a
        else :
            more, less = 'a', 'b'
            mn, ln = a, b
        if mn / (ln + 1) > 2:
            print("No possible solution") #Not required, as there will be no such input.
        while mn / ln != 1:
            res = res + more + more + less
            mn -= 2
            ln -= 1
            if mn == 0 or ln == 0:
                break

        while mn != 0 or ln != 0:
            if mn != 0:
                res = res + more
                mn -= 1
            if ln != 0:
                res = res + less
                ln -= 1

        return res


s = Solution()
print(s.strWithout3a3b(a=1, b=3))
print(s.strWithout3a3b(a=4, b=1))
print(s.strWithout3a3b(a=6, b=4))
print(s.strWithout3a3b(a=10, b=7))
print(s.strWithout3a3b(a=100, b=49))

