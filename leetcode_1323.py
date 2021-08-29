# Maximum 69 Number
class Solution:
    def maximum69Number(self, num: int) -> int:
        l = list(str(num))
        if l.count('6') == 0:
            return num
        else:
            ind = l.index('6')
            l[ind] = '9'
        return int(''.join(l))


s = Solution()
print(s.maximum69Number(num=9669))
print(s.maximum69Number(num=9996))
print(s.maximum69Number(num=9999))
