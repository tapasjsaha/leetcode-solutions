# Widest Vertical Area Between Two Points Containing No Points
class Solution:
    def maxWidthOfVerticalArea(self, points: [[int]]) -> int:
        xvalues = [point[0] for point in points]
        xvalues.sort()
        res = 0
        for i in range(1, len(xvalues), 1):
            x = xvalues[i] - xvalues[i - 1]
            res = max(res, x)
        return res


s1 = Solution()
print(s1.maxWidthOfVerticalArea(points=[[8, 7], [9, 9], [7, 4], [9, 7]]))
print(s1.maxWidthOfVerticalArea(points=[[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))
