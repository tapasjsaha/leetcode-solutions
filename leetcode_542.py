# 01 Matrix
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


    def updateMatrix(self, mat: [[int]]) -> [[int]]:
        lenr, lenc = len(mat), len(mat[0])
        queue = []
        for i in range(lenr):
            for j in range(lenc):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1
        level = 0
        while queue:
            level += 1
            ln = len(queue)
            for l in range(ln):
                x, y = queue.pop(0)
                for row, col in self.neighbours(x, y, lenr, lenc):
                    if mat[row][col] == -1:
                        mat[row][col] = level
                        queue.append((row, col))
        return mat


s = Solution()
mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
s.printmat(mat)
res = s.updateMatrix(mat)
s.printmat(res)

mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
s.printmat(mat)
res = s.updateMatrix(mat)
s.printmat(res)


"""

    def neighbours(self, r, c, lenr, lenc, dist):
        nodes = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        return [(x, y, dist+1) for x, y in nodes if 0 <= x < lenr and 0 <= y < lenc]


    def updateMatrix(self, mat: [[int]]) -> [[int]]:
        lenr, lenc = len(mat), len(mat[0])
        res = [[0 for i in range(lenc)] for j in range(lenr)]
        for i in range(lenr):
            for j in range(lenc):
                if mat[i][j] == 1:
                    queue = [(i, j, 0)]
                    visitted = set()
                    while queue:
                        x, y, d = queue.pop(0)
                        if mat[x][y] == 0:
                            res[i][j] = d
                            break
                        else:
                            nodes = self.neighbours(x, y, lenr, lenc, d)
                            for x, y, d in nodes:
                                if (x, y) not in visitted:
                                    visitted.add((x, y))
                                    queue.append((x, y, d))
        return res

"""
