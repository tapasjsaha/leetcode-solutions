# Destination City
class Solution:
    def destCity(self, paths: [[str]]) -> str:
        path = []
        p = paths.pop(0)
        path.append(p[0])
        path.append(p[1])
        while paths:
            p = paths.pop(0)
            if p[0] == path[-1]:
                path.append(p[1])
            elif p[1] == path[0]:
                path.insert(0, p[0])
            else:
                paths.append(p)
        return path[-1]


s = Solution()
print(s.destCity(paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
print(s.destCity(paths = [["B","C"],["D","B"],["C","A"]]))
print(s.destCity(paths = [["A","Z"]]))

print(s.destCity(paths=[["London", "New York"], ["Sao Paulo", "Delhi"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
