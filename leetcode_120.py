# Triangle
class Solution:
    def minimumTotal(self, triangle: [[int]]) -> int:
        while triangle:
            if len(triangle) == 1:
                return triangle[0][0]
            else:
                minpath = triangle.pop()
                res = []
                currpath = triangle.pop()
                for i in range(len(currpath)):
                    res.append(min(currpath[i]+minpath[i], currpath[i]+minpath[i+1]))
                triangle.append(res)


s = Solution()
print(s.minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(s.minimumTotal(triangle=[[-10]]))
