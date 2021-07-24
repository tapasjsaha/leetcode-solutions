# Print Words Vertically
class Solution:
    def printVertically(self, s: str) -> list:
        res = []
        words = s.split()
        ml = max([len(word) for word in words])
        pad = ' ' * ml
        for i in range(ml):
            s = ''.join([(word+pad)[i] for word in words])
            res.append(s.rstrip())
        return res


s = Solution()
print(s.printVertically(s="HOW ARE YOU"))
print(s.printVertically(s="TO BE OR NOT TO BE"))
print(s.printVertically(s="CONTEST IS COMING"))
print(s.printVertically(s="H"))
