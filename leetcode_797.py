# All Paths From Source to Target
class Solution:
    def allPathsSourceTarget(self, graph: [[int]]) -> [[int]]:
        target = len(graph) - 1
        paths = []

        def backtrack(current):
            if current[-1] == target:
                paths.append(current[:])
            else:
                candidate_list = graph[current[-1]]
                for candidate in candidate_list:
                    backtrack(current+[candidate])

        backtrack([0])
        return paths


s = Solution()
graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
print(s.allPathsSourceTarget(graph))

graph = [[2], [3], [1], []]
print(s.allPathsSourceTarget(graph))

graph = [[1,2], [3], [3], []]
print(s.allPathsSourceTarget(graph))




# target = len(graph) - 1
# paths = []
# queue = [[0]]
#
# while queue:
#     path = queue.pop(0)
#     connections = graph[path[-1]]
#     for connection in connections:
#         temp_path = path[:]
#         temp_path.extend([connection])
#         if temp_path[-1] == target:
#             paths.append(temp_path[:])
#         else:
#             queue.append(temp_path[:])
#         temp_path.clear()
# return paths