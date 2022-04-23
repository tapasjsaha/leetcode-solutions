# Check If It Is a Straight Line

class Solution:
    def checkStraightLine(self, coordinates: [[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        else:
            x1, y1 = coordinates[0][0], coordinates[0][1]
            x2, y2 = coordinates[1][0], coordinates[1][1]
            theta = (x2 - x1) / (y2 - y1) if (y2 - y1) != 0 else float('inf')
            for coordinate in coordinates[2:]:
                theta1 = (coordinate[0] - x1) / (coordinate[1] - y1) if (coordinate[1] - y1) != 0 else float('inf')
                if theta1 != theta:
                    return False
            return True


s = Solution()
print(s.checkStraightLine(coordinates=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))
print(s.checkStraightLine(coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(s.checkStraightLine(coordinates=[[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
print(s.checkStraightLine(coordinates=[[1, 1], [2, 2], [2, 1], [3, 2]]))
print(s.checkStraightLine(coordinates=[[1, 0], [2, 0], [3, 0], [4, 0]]))
print(s.checkStraightLine(coordinates=[[0, 1], [0, 2], [0, 3], [0, 4]]))
