# Remove All Occurrences of a Substring
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ln = len(part)
        stack = []
        for ch in s:
            stack.append(ch)
            if ''.join(stack[-ln:]) == part:
                for i in range(ln):
                    stack.pop()
        return ''.join(stack)


s = Solution()
print(s.removeOccurrences(s="daabcbaabcbc", part="abc"))
print(s.removeOccurrences(s="axxxxyyyyb", part="xy"))
