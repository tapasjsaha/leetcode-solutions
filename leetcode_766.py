# Toeplitz Matrix
class Solution:
    def isToeplitzMatrix(self, matrix: [[int]]) -> bool:
        row, col = len(matrix), len(matrix[0])
        if row == 1 or col == 1:
            return True
        else:
            prev = matrix[0]
            for curr in matrix[1:]:
                if curr[1:] != prev[:-1]:
                    return False
                prev = curr
            return True


s1 = Solution()
print(s1.isToeplitzMatrix(matrix=[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
print(s1.isToeplitzMatrix(matrix=[[1, 2], [2, 2]]))
