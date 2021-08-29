# Number of Segments in a String
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


s = Solution()
print(s.countSegments(s="Hello, my name is John"))
