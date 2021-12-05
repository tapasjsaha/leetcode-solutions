# Shortest Path in Binary Matrix
class Solution:
    def printmat(self, mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                print(mat[i][j], end=" ")
            print("")
        print("------------------")
        return None

    def shortestPathBinaryMatrix(self, grid: [[int]]) -> int:

        def neighbours(r, c, lenr, lenc):
            nodes = [(r + 1, c + 1), (r + 1, c - 1), (r - 1, c + 1), (r - 1, c - 1),
                     (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            return [(x, y) for x, y in nodes if 0 <= x < lenr and 0 <= y < lenc]

        lenr, lenc = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[lenr - 1][lenc - 1] == 1:
            return -1

        path = 0
        visited = set()
        visited.add((0, 0))
        queue = [(0, 0)]
        while queue:
            path += 1
            for i in range(len(queue)):
                (row, col) = queue.pop(0)
                if row == lenr - 1 and col == lenc - 1:
                    return path
                else:
                    for (x, y) in neighbours(row, col, lenr, lenc):
                        if grid[x][y] == 0 and (x, y) not in visited:
                            queue.append((x, y))
                            visited.add((x, y))
        return -1


s = Solution()
grid = [[0, 1], [1, 0]]
s.printmat(grid)
res = s.shortestPathBinaryMatrix(grid)
print(res)

grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
s.printmat(grid)
res = s.shortestPathBinaryMatrix(grid)
print(res)

grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
s.printmat(grid)
res = s.shortestPathBinaryMatrix(grid)
print(res)

grid = [[0, 0, 0], [1, 1, 1], [1, 1, 0]]
s.printmat(grid)
res = s.shortestPathBinaryMatrix(grid)
print(res)
