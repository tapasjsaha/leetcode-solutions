# Surrounded Regions

class Solution:
    def printmat(self, mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                print(mat[i][j], end=" ")
            print("")
        print("------------------")
        return None

    def solve(self, board: [[str]]) -> None:
        """Do not return anything, modify board in-place instead."""
        lenr, lenc = len(board), len(board[0])

        def neighbours(row, col, lenr, lenc):
            nodes = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            return [(x, y) for (x, y) in nodes if 0 <= x < lenr and 0 <= y < lenc]

        # Loop through the matrix to search for "O" in the border
        queue = []
        # Top and bottom row
        for r in range(lenr):
            for c in range(lenc):
                if r in [0, lenr-1] or c in [0, lenc-1]:
                    if board[r][c] == "O":
                        board[r][c] = "Q"
                        queue.append((r, c))
                        while queue:
                            (x, y) = queue.pop(0)
                            for (row, col) in neighbours(x, y, lenr, lenc):
                                if board[row][col] == "O":
                                    board[row][col] = "Q"
                                    queue.append((row, col))

        # Replace all "Q" with "O" and remaining "O" with "X"
        for i in range(lenr):
            for j in range(lenc):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Q":
                    board[i][j] = "O"

        return None


s = Solution()
board = [["X", "X", "X", "X", "X", "X"], ["X", "O", "O", "X", "X", "O"],
         ["X", "X", "O", "X", "X", "X"], ["X", "O", "X", "X", "O", "O"],
         ["X", "X", "O", "X", "X", "X"], ["X", "X", "O", "X", "O", "X"]]
s.printmat(board)
s.solve(board)
s.printmat(board)
