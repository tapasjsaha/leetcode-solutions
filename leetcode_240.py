# Search a 2D Matrix II
class Solution:
    def printmat(self, mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                print(mat[i][j], end=" ")
            print("")
        print("------------------")
        return None

    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        hight = len(matrix)
        width = len(matrix[0])
        previous = (-1, -1)
        row, col = 0, width-1
        while 0 <= row < hight and 0 <= col < width:
            if matrix[row][col] == target:
                return True
            else:
                if matrix[row][col] > target:
                    col -= 1
                else:
                    row += 1
                if (row, col) == previous:
                    break
                else:
                    previous = (row, col)
        return False


s = Solution()
matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
s.printmat(matrix)
print(s.searchMatrix(matrix, target=5))
print(s.searchMatrix(matrix, target=21))
print(s.searchMatrix(matrix, target=20))
print(s.searchMatrix(matrix, target=31))


matrix = [[1]]
s.printmat(matrix)
print(s.searchMatrix(matrix, target=5))

matrix = [[-5]]
s.printmat(matrix)
print(s.searchMatrix(matrix, target=-10))