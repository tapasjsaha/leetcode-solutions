# Determine whether matrix can be obtained by rotation

class Solution:
    @staticmethod
    def printmat(mat):
        """Print the matrix"""
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                print(mat[i][j], end=" ")
            print("")
        print("------------------")
        return None

    @staticmethod
    def rotate(mat):
        """Rotate the matrix clockwise 90 degree"""
        hight = len(mat)
        width = len(mat[0])
        """swap the elements vertically"""
        for j in range(width):
            for i in range(hight // 2):
                mat[i][j], mat[hight - 1 - i][j] = mat[hight - 1 - i][j], mat[i][j]
        """Transpose the matrix"""
        for j in range(width):
            for i in range(j + 1, hight):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        return mat

    def findRotation(self, mat: [[int]], target: [[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            else:
                self.rotate(mat)
        return False


s = Solution()

matrix = [[0, 1], [1, 0]]
target = [[1, 0], [0, 1]]
print(s.findRotation(matrix, target))

matrix = [[0, 1], [1, 1]]
target = [[1, 0], [0, 1]]
print(s.findRotation(matrix, target))

matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
print(s.findRotation(matrix, target))

matrix = [[1]]
target = [[1]]
print(s.findRotation(matrix, target))

matrix = [[1]]
target = [[0]]
print(s.findRotation(matrix, target))
