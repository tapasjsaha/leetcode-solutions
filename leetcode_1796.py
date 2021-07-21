# Second Largest Digit in a String
class Solution:
    def secondHighest(self, s: str) -> int:
        chars = set(s)
        l = [int(x) for x in chars if x.isdigit()]
        if len(l) < 2:
            return -1
        else:
            l.remove(max(l))
            return max(l)


s = Solution()
print(s.secondHighest(s="dfa12321afd"))
print(s.secondHighest(s="abc1111"))
print(s.secondHighest(s="a"))
