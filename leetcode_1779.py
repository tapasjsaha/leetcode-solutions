# Find Nearest Point That Has the Same X or Y Coordinate
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: [[int]]) -> int:
        valid = [(point, i) for i, point in enumerate(points) if point[0] == x or point[1] == y]
        if not valid:
            return -1
        else:
            valid.sort(key=lambda a: (abs(a[0][0]-x) + abs(a[0][1]-y), a[1]))
        return points.index(valid[0][0])


s = Solution()
print(s.nearestValidPoint(x=3, y=4, points=[[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]))
print(s.nearestValidPoint(x=3, y=4, points=[[3, 4]]))
print(s.nearestValidPoint(x=3, y=4, points=[[2, 3]]))
