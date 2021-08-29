# Find the Town Judge
class Solution:
    def findJudge(self, n: int, trust: [[int]]) -> int:
        trust_matrix = []
        for i in range(n):
            c = []
            for j in range(n):
                c.append(0)
            trust_matrix.append(c)
        for e in trust:
            trust_matrix[e[0] - 1][e[1] - 1] += 1
        # for _ in trust_matrix:
        #    print(_)

        i = 0
        while i < n:
            if sum(trust_matrix[i][:]) == 0:
                break
            i += 1
        if i == n:
            return -1
        else:
            j = i
            if sum([trust_matrix[x][j] for x in range(n)]) == n - 1:
                return j + 1
            else:
                return -1


s = Solution()
print(s.findJudge(n=2, trust=[[1, 2]]))
print(s.findJudge(n=3, trust=[[1, 3], [2, 3]]))
print(s.findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]))
print(s.findJudge(n=3, trust=[[1, 2], [2, 3]]))
print(s.findJudge(n=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
