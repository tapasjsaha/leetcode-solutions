# Rotting Oranges
class Solution:
    def printmat(self, mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                print(mat[i][j], end=" ")
            print("")
        print("------------------")
        return None

    def neighbours(self, r, c, lenr, lenc):
        nodes = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        return [(x, y) for x, y in nodes if 0 <= x < lenr and 0 <= y < lenc]

    def orangesRotting(self, grid: [[int]]) -> int:
        lenr, lenc = len(grid), len(grid[0])
        time = 0
        queue = [(i, j) for i in range(lenr) for j in range(lenc) if grid[i][j] == 2]

        while queue:
            ln, check = len(queue), False
            for l in range(ln):
                x, y = queue.pop(0)
                for row, col in self.neighbours(x, y, lenr, lenc):
                    if grid[row][col] == 1:
                        grid[row][col] = 2
                        queue.append((row, col))
                        check = True
            # self.printmat(grid)
            time += 1 if check else 0

        queue = [(i, j) for i in range(lenr) for j in range(lenc) if grid[i][j] == 1]
        time = time if not queue else -1
        return time


s = Solution()
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(s.orangesRotting(grid))

s = Solution()
grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
print(s.orangesRotting(grid))

s = Solution()
grid = [[0, 2]]
print(s.orangesRotting(grid))
