# Minimum Number of Vertices to Reach All Nodes
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: [[int]]) -> [int]:
        d = {}
        for i in range(n):
            d[i] = 0
        for edge in edges:
            d[edge[1]] += 1
        return [key for key, val in d.items() if val == 0]


s = Solution()
print(s.findSmallestSetOfVertices(n=6, edges=[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))  # [0,3]
print(s.findSmallestSetOfVertices(n=5, edges=[[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))  # [0,2,3]
print(s.findSmallestSetOfVertices(n=6, edges=[[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))  # [0,2,3,5]
