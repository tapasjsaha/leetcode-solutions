# N-Queens II
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []

        def backtrack(current, posDiag, negDiag):
            if len(current) == n:
                res.append(current[:])
            else:
                candidate_list = []
                pos = len(current)
                for i in range(n):
                    if i not in current and i+pos not in posDiag and i-pos not in negDiag:
                        candidate_list.append(i)

                for candidate in candidate_list:
                    posDiag.add(candidate + pos)
                    negDiag.add(candidate - pos)
                    backtrack(current+[candidate], posDiag, negDiag)
                    posDiag.remove(candidate + pos)
                    negDiag.remove(candidate - pos)

        backtrack([], set(), set())
        return len(res)


s = Solution()
print(s.totalNQueens(n=1))
print(s.totalNQueens(n=2))
print(s.totalNQueens(n=3))
print(s.totalNQueens(n=4))
print(s.totalNQueens(n=5))
print(s.totalNQueens(n=6))
print(s.totalNQueens(n=7))
print(s.totalNQueens(n=8))
print(s.totalNQueens(n=9))

