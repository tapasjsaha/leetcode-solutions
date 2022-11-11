# Transpose Matrix
class Solution:
    def transpose(self, matrix: [[int]]) -> [[int]]:
        rows, cols = len(matrix), len(matrix[0])
        res = []
        for c in range(cols):
            temp = []
            for r in range(rows):
                temp.append(matrix[r][c])
            res.append(temp)
        return res


s = Solution()
print(s.transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.transpose(matrix=[[1, 2, 3], [4, 5, 6]]))
