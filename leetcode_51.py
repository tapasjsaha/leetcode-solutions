# N-Queens
class Solution:
    def solveNQueens(self, n):
        sol = []
        res = []

        def backtrack(current, pos_dig, neg_dig):
            if len(current) == n:
                sol.append(current[:])
            else:
                # construct candidates
                j = len(current)
                candidate_list = [x for x in range(n) if x not in current and j+x not in pos_dig and j-x not in neg_dig]
                # main loop
                for candidate in candidate_list:
                    pos_dig.add(j+candidate)
                    neg_dig.add(j-candidate)
                    backtrack(current+[candidate], pos_dig, neg_dig)
                    pos_dig.remove(j + candidate)
                    neg_dig.remove(j - candidate)

        backtrack([], set(), set())

        for s in sol:
            board = [['.'] * n for i in range(n)]
            for col, row in enumerate(s):
                board[row][col] = 'Q'
            temp = []
            for row in board:
                temp.append(''.join(row))
            res.append(temp)

        return res


s = Solution()
print(s.solveNQueens(4))
#print(s.nqueen(9))
