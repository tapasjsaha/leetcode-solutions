# Check If Word Is Valid After Substitutions
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            stack.append(c)
            if ''.join(stack[-3:]) == 'abc':
                stack = stack[:len(stack) - 3]
        return not stack


s = Solution()
print(s.isValid(s="aabcbc"))
print(s.isValid(s="abcabcababcc"))
print(s.isValid(s="abccba"))
print(s.isValid(s="cababc"))
