# Rotate Image
class Solution:
    def printmat(self, mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                print(mat[i][j], end=" ")
            print("")
        print("------------------")
        return None

    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hight = len(matrix)
        width = len(matrix[0])

        # Anticlock wise rotetion : First swap left to right, then swap accross the symetry
#        for i in range(hight):
#            for j in range(width//2):
#                matrix[i][j], matrix[i][width-1-j] = matrix[i][width-1-j], matrix[i][j]
#        for i in range(hight):
#            for j in range(i+1, width):
#                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Clock wise rotetion : First swap top to bottom, then swap accross the symetry
        for j in range(width):
            for i in range(hight // 2):
                matrix[i][j], matrix[hight - 1 - i][j] = matrix[hight - 1 - i][j], matrix[i][j]
        for i in range(hight):
            for j in range(i + 1, width):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix


s = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s.printmat(matrix)
matrix1 = s.rotate(matrix)
s.printmat(matrix1)

matrix = [[1]]
s.printmat(matrix)
matrix1 = s.rotate(matrix)
s.printmat(matrix1)

matrix = [[1, 2], [3, 4]]
s.printmat(matrix)
matrix1 = s.rotate(matrix)
s.printmat(matrix1)

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
s.printmat(matrix)
matrix1 = s.rotate(matrix)
s.printmat(matrix1)
