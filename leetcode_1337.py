# The K Weakest Rows in a Matrix
class Solution:
    def kWeakestRows(self, mat: [[int]], k: int) -> [int]:
        res = []
        for i, v in enumerate(mat):
            res.append((sum(v), i))
        res.sort(key=lambda x: (x[0], x[1]))
        r = [x[1] for x in res]
        return r[:k]


s = Solution()
print(s.kWeakestRows(mat=
                     [[1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 0],
                      [1, 0, 0, 0, 0],
                      [1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 1]],
                     k=3))

print(s.kWeakestRows(mat=
                     [[1, 0, 0, 0],
                      [1, 1, 1, 1],
                      [1, 0, 0, 0],
                      [1, 0, 0, 0]],
                     k=2))
