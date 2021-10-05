# Reshape the Matrix
class Solution:
    def matrixReshape(self, mat: [[int]], r: int, c: int) -> [[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        else:
            res = [mat[i][j] for i in range(m) for j in range(n)]
            mat, i = [], 0
            for row in range(r):
                temp = []
                for col in range(c):
                    temp.append(res[i])
                    i += 1
                mat.append(temp)
        return mat


s = Solution()
print(s.matrixReshape(mat=[[1, 2], [3, 4]], r=1, c=4))
print(s.matrixReshape(mat=[[1, 2], [3, 4]], r=2, c=4))
