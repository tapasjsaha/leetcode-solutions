# Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while True:
            for i in range(left, right, 1):
                res.append(matrix[top][i])
            top += 1
            if top == bottom: break
            for j in range(top, bottom, 1):
                res.append(matrix[j][right - 1])
            right -= 1
            if left == right: break
            for k in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][k])
            bottom -= 1
            if top == bottom: break
            for l in range(bottom - 1, top - 1, -1):
                res.append(matrix[l][left])
            left += 1
            if left == right: break
        return res


s = Solution()
print(s.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))  # [1,2,3,4,8,12,11,10,9,5,6,7]
print(s.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1,2,3,6,9,8,7,4,5]
print(s.spiralOrder(matrix=[[1]]))  # [1]
print(s.spiralOrder(matrix=[[1, 2, 3]]))  # [1,2,3]
print(s.spiralOrder(matrix=[[1], [2], [3]]))  # [1,2,3]