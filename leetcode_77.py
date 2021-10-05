# Combinations
class Solution:
    def combine(self, n: int, k: int) -> [[int]]:
        res = []
        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb[:])
            else:
                for i in range(start, n+1, 1):
                    comb.append(i)
                    backtrack(i+1, comb)
                    comb.pop()

        backtrack(1, [])
        return res


s = Solution()
print(s.combine(4, 2))
