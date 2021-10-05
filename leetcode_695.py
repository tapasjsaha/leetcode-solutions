# Max Area of Island
class Solution:
    def dfs(self, grid, r, c, lenr, lenc):
        grid[r][c] = 0
        area = 1
        neighbours = [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]
        for x, y in neighbours:
            if 0 <= x < lenr and 0 <= y < lenc and grid[x][y] == 1:
                area += self.dfs(grid, x, y, lenr, lenc)
        return area

    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        lenr, lenc = len(grid), len(grid[0])
        max_area = 0
        for r in range(lenr):
            for c in range(lenc):
                if grid[r][c] == 1:
                    max_area = max(max_area, self.dfs(grid, r, c, lenr, lenc))
        return max_area


s = Solution()
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

print(s.maxAreaOfIsland(grid))

grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
print(s.maxAreaOfIsland(grid))

