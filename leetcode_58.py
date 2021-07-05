#Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.strip().split(" ")
        return len(lst[-1])


s = Solution()
print(s.lengthOfLastWord(""))
print(s.lengthOfLastWord("   "))
print(s.lengthOfLastWord("This is my last word"))
