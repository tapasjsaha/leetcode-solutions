# Spiral Matrix II
class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        matrix = [[1 for i in range(n)] for j in range(n)]
        left, right, top, bottom = 0, n, 0, n
        x = 1
        while True:
            for i in range(left, right, 1):
                matrix[top][i] *= x
                x += 1
            top += 1
            if top == bottom: break
            for j in range(top, bottom, 1):
                matrix[j][right - 1] *= x
                x += 1
            right -= 1
            if left == right: break
            for k in range(right - 1, left - 1, -1):
                matrix[bottom - 1][k] *= x
                x += 1
            bottom -= 1
            if top == bottom: break
            for l in range(bottom - 1, top - 1, -1):
                matrix[l][left] *= x
                x += 1
            left += 1
            if left == right: break
        return matrix


s = Solution()
print(s.generateMatrix(3))  # [[1,2,3],[8,9,4],[7,6,5]]
print(s.generateMatrix(1))  # [[1]]