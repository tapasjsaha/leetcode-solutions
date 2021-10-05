# Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        row, lenr, lenc = 0, len(matrix), len(matrix[0])
        # Check row
        for r in range(lenr-1):
            if target >= matrix[row+1][0]:
                row += 1
            else:
                break
        # Check all columns for selected row
        for col in range(lenc):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                return False
        return False


s = Solution()
print(s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
print(s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
print(s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=70))
