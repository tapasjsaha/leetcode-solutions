# Excel Sheet Column Title
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dic = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I',
               10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q',
               18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
               0: 'Z'}
        res = []
        rem = -1
        while columnNumber != 0:
            rem = columnNumber % 26
            columnNumber = columnNumber // 26 - 1 if rem == 0 else columnNumber // 26
            res.append(rem)
        res.reverse()
        #print(res)
        col = [dic[r] for r in res]
        return ''.join(col)


s = Solution()
print(s.convertToTitle(columnNumber=1))
print(s.convertToTitle(columnNumber=26))
print(s.convertToTitle(columnNumber=27))
print(s.convertToTitle(columnNumber=28))
print(s.convertToTitle(columnNumber=52))
print(s.convertToTitle(columnNumber=78))
print(s.convertToTitle(columnNumber=701))
print(s.convertToTitle(columnNumber=702))
print(s.convertToTitle(columnNumber=2147483647))
