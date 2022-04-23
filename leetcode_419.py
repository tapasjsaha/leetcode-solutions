# Battleships in a Board
class Solution:
    def countBattleships(self, board: [[str]]) -> int:
        def neighbours(row, col, lenr, lenc):
            nodes = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            return [node for node in nodes if 0 <= node[0] < lenr and 0 <= node[1] < lenc]

        def dfs(row, col, lenr, lenc):
            stack = [(row, col)]
            while stack:
                r, c = stack.pop(0)
                if board[r][c] == 'X':
                    visited.add((r, c))
                    for node in neighbours(r, c, lenr, lenc):
                        if (node[0], node[1]) not in visited:
                            stack.append((node[0], node[1]))

        lenr, lenc = len(board), len(board[0])
        visited = set()
        count = 0
        print(lenr, lenc)
        for row in range(lenr):
            for col in range(lenc):
                if (row, col) not in visited and board[row][col] == 'X':
                    count += 1
                    dfs(row, col, lenr, lenc)
                else:
                    visited.add((row, col))

        return count


s = Solution()
print(s.countBattleships(board=[["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
print(s.countBattleships(board=[["X", ".", ".", "X"], [".", ".", ".", "X"], ["X", "X", ".", "X"]]))
print(s.countBattleships(board=[["."]]))
