# Word Search
class Solution:
    def printBoard(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j], end=" ")
            print()


    def exist(self, board: [[str]], word: str) -> bool:
        lenr, lenc = len(board), len(board[0])
        path = set()

        def dfs(row, col, i):
            if i == len(word):
                return True
            if row < 0 or col < 0 or row >= lenr or col >= lenc or board[row][col] != word[i] or (row, col) in path:
                return False

            path.add((row, col))
            res = (dfs(row + 1, col, i + 1) or dfs(row - 1, col, i + 1)
                   or dfs(row, col + 1, i + 1) or dfs(row, col - 1, i + 1))
            path.remove((row, col))
            return res

        for r in range(lenr):
            for c in range(lenc):
                if dfs(r, c, 0):
                    return True
        return False

s = Solution()
board = [["A", "B"], ["S", "F"]]
s.printBoard(board)
print(s.exist(board, word="S"))

s = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
s.printBoard(board)
print(s.exist(board, word="ABCCED"))

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
s.printBoard(board)
print(s.exist(board, word="SEE"))

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
s.printBoard(board)
print(s.exist(board, word="ABCB"))






# def printBoard(self, board):
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             print(board[i][j], end=" ")
#         print()
#
#
# def exist(self, board: [[str]], word: str) -> bool:
#     lenr, lenc = len(board), len(board[0])
#     path = set()
#
#     def dfs(row, col, i):
#         if i == len(word):
#             return True
#         if row < 0 or col < 0 or row >= lenr or col >= lenc or board[row][col] != word[i] or (row, col) in path:
#             return False
#
#         path.add((row, col))
#         res = (dfs(row + 1, col, i + 1) or dfs(row - 1, col, i + 1)
#                or dfs(row, col + 1, i + 1) or dfs(row, col - 1, i + 1))
#         path.remove((row, col))
#         return res
#
#     for r in range(lenr):
#         for c in range(lenc):
#             if dfs(r, c, 0):
#                 return True
#     return False