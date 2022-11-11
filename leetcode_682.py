# Baseball Game
class Solution:
    def calPoints(self, ops: [str]) -> int:
        res = []
        for ch in ops:
            if ch == '+':
                a = res[-1]
                b = res[-2]
                res.append(a + b)
            elif ch == 'D':
                a = res[-1]
                res.append(2 * a)
            elif ch == 'C':
                res.pop()
            else:
                res.append(int(ch))
        return sum(res)


s = Solution()
print(s.calPoints(ops=["5", "2", "C", "D", "+"]))
print(s.calPoints(ops=["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(s.calPoints(ops=["1","C"]))
