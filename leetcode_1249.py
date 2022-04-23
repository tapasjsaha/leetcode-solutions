# Minimum Remove to Make Valid Parentheses
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, v in enumerate(s):
            if v == '(':
                stack.append(('(', i))
            elif v == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((')', i))
            else:
                pass
        # print(stack)
        strng = list(s)
        for i in range(len(stack) - 1, -1, -1):
            a, b = stack[i]
            strng.pop(b)

        return ''.join(strng)


s = Solution()
print(s.minRemoveToMakeValid(s="lee(t(c)o)de)"))
print(s.minRemoveToMakeValid(s="a)b(c)d"))
print(s.minRemoveToMakeValid(s="))(("))
