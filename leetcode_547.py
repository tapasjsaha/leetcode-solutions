# Number of Provinces
class Solution:
    def findCircleNum(self, isConnected: [[int]]) -> int:
        province = 0
        visited = set()
        queue = []
        lenr = lenc = len(isConnected)  # n * n matrix

        for i in range(lenr):
            if i not in visited:
                province += 1
                visited.add(i)
                queue.append(i)
                while queue:
                    row = queue.pop(0)
                    for col in range(0, lenc, 1):
                        if isConnected[row][col] == 1 and col not in visited:
                            queue.append(col)
                            visited.add(col)
        return province


s = Solution()
print(s.findCircleNum(isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(s.findCircleNum(isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(s.findCircleNum(isConnected=[[1, 0, 0, 1],
                                   [0, 1, 1, 0],
                                   [0, 1, 1, 1],
                                   [1, 0, 1, 1]]))
