# Flood Fill
class Solution:
    @staticmethod
    def neighbours(r, c, lenr, lenc):
        """Calculate and return the neighbours of the current index"""
        neighbours = [[r - 1, c], [r, c - 1], [r, c + 1], [r + 1, c]]
        valid = [[x, y] for x, y in neighbours if (0 <= x < lenr) and (0 <= y < lenc)]
        return valid

    def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
        print(image)
        stack = [[sr, sc]]
        currcolor = image[sr][sc]
        lenr, lenc = len(image), len(image[0])
        visited = set()
        while stack:
            (x, y) = stack.pop()
            if (x, y) not in visited:
                visited.add((x, y))
                image[x][y] = newColor
                moves = self.neighbours(x, y, lenr, lenc)
                for move in moves:
                    if image[move[0]][move[1]] == currcolor:
                        stack.append([move[0], move[1]])
        return image


s = Solution()
print(s.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2))
