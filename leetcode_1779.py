# Find Nearest Point That Has the Same X or Y Coordinate
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: [[int]]) -> int:
        res = -1
        distance = float('inf')
        for ind, point in enumerate(points):
            if point[0] == x or point[1] == y:
                d = abs(x-point[0]+y-point[1])
                if d < distance:
                    res = ind
                    distance = d
        return res


s = Solution()
print(s.nearestValidPoint(x=3, y=4, points=[[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]))
print(s.nearestValidPoint(x=3, y=4, points=[[3, 4]]))
print(s.nearestValidPoint(x=3, y=4, points=[[2, 3]]))
