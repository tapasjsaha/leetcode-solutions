# Maximum Nesting Depth of the Parentheses
class Solution:
    def maxDepth(self, s: str) -> int:
        counter, ans = 0, 0
        for ch in s:
            if ch == '(':
                counter += 1
                ans = max(counter, ans)
            elif ch == ')':
                counter -= 1
            else:
                pass
        return ans


s = Solution()
print(s.maxDepth(s="(1+(2*3)+((8)/4))+1"))
print(s.maxDepth(s="(1)+((2))+(((3)))"))
