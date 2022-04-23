# Matrix Diagonal Sum
class Solution:
    def diagonalSum(self, mat: [[int]]) -> int:
        lenside = len(mat)
        total = 0
        for i in range(lenside):
            total += mat[i][i]
            total += mat[i][lenside - i -1]

        if lenside % 2 == 1:
            mid = lenside // 2
            total -= mat[mid][mid]

        return total


s = Solution()
print(s.diagonalSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.diagonalSum(mat=[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
print(s.diagonalSum(mat=[[5]]))
