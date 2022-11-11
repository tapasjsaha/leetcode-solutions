# Check if Matrix Is X-Matrix
class Solution:
    def checkXMatrix(self, grid: [[int]]) -> bool:
        row, col = len(grid), len(grid[0])
        N = row - 1
        for r in range(row):
            for c in range(col):
                if r == c or r + c == N:
                    # diagonal element
                    if grid[r][c] == 0:
                        return False
                else:
                    # non diagonal element
                    if grid[r][c] != 0:
                        return False
        return True


s = Solution()
print(s.checkXMatrix(grid=[[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]))
print(s.checkXMatrix(grid=[[5, 7, 0], [0, 3, 1], [0, 5, 0]]))
