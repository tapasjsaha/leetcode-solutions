# Number of Islands
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        res, lenr, lenc = 0, len(grid), len(grid[0])
        visited = set()
        queue = []
        # print(lenr, lenc)

        def neighbours(row, col):
            near = [[row, col + 1], [row, col - 1], [row + 1, col], [row - 1, col]]
            return [x for x in near if ((0 <= x[0] < lenr) and (0 <= x[1] < lenc) and grid[x[0]][x[1]] == '1')]

        for i in range(lenr):
            for j in range(lenc):
                if grid[i][j] == '1' and (i, j) not in visited:
                    res += 1
                    queue.append([i, j])
                    visited.add((i, j))
                    while queue:
                        [row, col] = queue.pop(0)
                        for point in neighbours(row, col):
                            if (point[0], point[1]) not in visited:
                                queue.append([point[0], point[1]])
                                visited.add((point[0], point[1]))
        return res


s = Solution()
print(s.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "1"]
]))
