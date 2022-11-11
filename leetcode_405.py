# Convert a Number to Hexadecimal
class Solution:
    def toHex(self, num: int) -> str:
        d = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c',
             13: 'd', 14: 'e', 15: 'f'}
        res = '' if num != 0 else '0'
        if num < 0:
            x = (1 << 32) + num
            # x = (1 << 32) - 1
            # x = (-num ^ x) + 1
        else:
            x = num
        while x != 0:
            c = x % 16
            x = x // 16
            res = d[c] + res
        return res


s = Solution()
print(s.toHex(num=26))
print(s.toHex(num=-1))
print(s.toHex(num=0))
print(s.toHex(num=2**30-1))
