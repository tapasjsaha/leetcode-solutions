# K Closest Points to Origin
class Solution:
    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        list_of_points = [[x, y, x * x + y * y] for x, y in points]
        list_of_points.sort(key=lambda x: x[2], reverse=False)
        return [[x, y] for x, y, d in list_of_points[:k]]


s = Solution()
print(s.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))
print(s.kClosest(points=[[1, 3], [-2, 2]], k=1))
