# Check if All the Integers in a Range Are Covered
class Solution:
    def isCovered(self, ranges: [[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1, 1):
            for r in ranges:
                if i >= r[0] and i <= r[1]:
                    break
            else:
                return False
        return True


s = Solution()
print(s.isCovered(ranges=[[1, 2], [3, 4], [5, 6]], left=2, right=5))
print(s.isCovered(ranges=[[1, 10], [10, 20]], left=21, right=21))
