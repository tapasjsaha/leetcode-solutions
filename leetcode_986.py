# Interval List Intersections

# As the intervals are disjoint for any point in firstlist there can be only one interval

class Solution:
    def intervalIntersection(self, firstList: [[int]], secondList: [[int]]) -> [[int]]:
        res = []
        if not firstList or not secondList:
            return res
        else:
            i, lenf, j, lens = 0, len(firstList), 0, len(secondList)
            while i < lenf and j < lens:
                low = max(firstList[i][0], secondList[j][0])
                high = min(firstList[i][1], secondList[j][1])
                if low <= high:
                    res.append([low, high])
                if firstList[i][1] < secondList[j][1]:
                    i += 1
                else:
                    j += 1
        return res


s = Solution()
print(s.intervalIntersection(firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
                             secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]))

print(s.intervalIntersection(firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
                             secondList=[]))

print(s.intervalIntersection(firstList=[],
                             secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]))

print(s.intervalIntersection(firstList=[[2, 20]],
                             secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]))
