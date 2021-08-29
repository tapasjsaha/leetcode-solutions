# Excel Sheet Column Number
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
             'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
             'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
        title = list(columnTitle)
        while title:
            x = d[title.pop(0)]
            res = res * 26 + x
        return res


s = Solution()
print(s.titleToNumber(columnTitle="A"))
print(s.titleToNumber(columnTitle="AB"))
print(s.titleToNumber(columnTitle="ZY"))
print(s.titleToNumber(columnTitle="FXSHRXW"))
print(s.titleToNumber(columnTitle="AA"))
print(s.titleToNumber(columnTitle="CB"))
print(s.titleToNumber(columnTitle="ZZ"))
print(s.titleToNumber(columnTitle="AAA"))
