# Find the Difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lst = list(t)
        for ch in s:
            lst.remove(ch)
        return ''.join(lst)


s = Solution()
print(s.findTheDifference(s="abcd", t="abcde"))
print(s.findTheDifference(s="", t="y"))
