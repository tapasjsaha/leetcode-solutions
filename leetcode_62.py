# https://www.youtube.com/watch?v=fEcyKrdIkho
# Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row, col = max(m, n), min(m, n)
        # Create row 1:
        arr = [1] * col
        # arr[0] = 0

        for i in range(row-1):
            arr[0] = 1
            for j in range(1, col, 1):
                arr[j] = arr[j]+arr[j-1]
            # print(arr)
        # print("------------- Final -------------")
        # print(arr)
        return arr[-1]


s = Solution()
print(s.uniquePaths(m=3, n=7))
print(s.uniquePaths(m=3, n=2))
print(s.uniquePaths(m=3, n=3))
print(s.uniquePaths(m=1, n=1))
