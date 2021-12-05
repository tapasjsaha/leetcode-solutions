# K-th Symbol in Grammar
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        from math import ceil
        if n == 1 and k == 1:
            return 0
        else:
            prev = self.kthGrammar(n - 1, ceil(k / 2))
            if prev == 0:
                return 1 if k % 2 == 0 else 0
            else:
                return 0 if k % 2 == 0 else 1


s = Solution()
print(s.kthGrammar(n=1, k=1))
print(s.kthGrammar(n=2, k=2))

print(s.kthGrammar(n=4, k=1))

print(s.kthGrammar(n=5, k=12))
