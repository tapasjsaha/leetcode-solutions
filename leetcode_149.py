# Max Points on a Line
class Solution:
    def maxPoints(self, points: [[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        else:
            # print(points)
            # create dictionary of lines for each point (slope is the key and number of points is the value)
            max_points = 0
            for i, point in enumerate(points):
                lines = {}
                local_max = 0
                for j in range(0, i, 1):
                    # print(point, points[j])
                    xdiff = point[0] - points[j][0]
                    ydiff = point[1] - points[j][1]
                    slope = (ydiff / xdiff) if xdiff != 0 else 'inf'
                    # print(point1, point2, slope)
                    if slope in lines:
                        lines[slope] += 1
                    else:
                        lines[slope] = 2

                for v in lines.values():
                    if v > max_points:
                        max_points = v

            return max_points

            # maxpoints = 0
            # for v in lines.values():
            #    if len(v) > maxpoints:
            #        maxpoints = len(v)


s = Solution()
print(s.maxPoints(points=[[1, 1]]))
print(s.maxPoints(points=[[1, 1], [4, 2], [3, 3]]))
print(s.maxPoints(points=[[1, 1], [2, 2], [3, 3]]))  # 3
print(s.maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))  # 4
print(s.maxPoints(points=[[0, 0], [4, 5], [7, 8], [8, 9], [5, 6], [3, 4], [1, 1]]))

# T0 under stand and visualize the result/points
# if len(points) <= 2:
#    return len(points)
# else:
#    print(points)
#    # create dictionary of lines for each point (slope is the key and number of points is the value)
#    max_points = 0
#    for i, point in enumerate(points):
#        lines = {}
#        for j in range(0, i, 1):
#            # print(point, points[j])
#            xdiff = point[0] - points[j][0]
#            ydiff = point[1] - points[j][1]
#            slope = (ydiff / xdiff) if xdiff != 0 else 'inf'
#            # print(point1, point2, slope)
#            if slope in lines:
#                lines[slope].add((points[j][0], points[j][1]))
#            else:
#                s = set()
#                s.add((point[0], point[1]))
#                s.add((points[j][0], points[j][1]))
#                lines[slope] = s
#        print(lines)
