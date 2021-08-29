# Basic Calculator II
class Solution:
    def calculate(self, s: str) -> int:
        op = ['+', '-', '*', '/']
        stack = []

        # Separating numbers and operators
        for ch in s:
            if ch in op:
                stack.append(ch)
            elif ch == ' ':
                continue
            else:
                if stack and stack[-1] not in op:
                    x = stack.pop()
                    stack.append(x * 10 + int(ch))
                else:
                    stack.append(int(ch))

        # Performing '*' and '/' operation first
        if '*' in stack or '/' in stack:
            temp = []
            i = 0
            while i < len(stack):
                if stack[i] in ['*', '/']:
                    x = temp.pop()
                    if stack[i] == '*':
                        temp.append(x*stack[i+1])
                    else:
                        temp.append(x//stack[i+1])
                    i += 1
                else:
                    temp.append(stack[i])
                i += 1
            stack = temp

        # Performing '+' and '-' operation
        if '+' in stack or '-' in stack:
            temp = []
            i = 0
            while i < len(stack):
                if stack[i] in ['+', '-']:
                    x = temp.pop()
                    if stack[i] == '+':
                        temp.append(x+stack[i+1])
                    else:
                        temp.append(x-stack[i+1])
                    i += 1
                else:
                    temp.append(stack[i])
                i += 1
            stack = temp
        return stack[0]


s = Solution()
print(s.calculate(s="301+20*2"))
print(s.calculate(s="3+2*2"))
print(s.calculate(s=" 3/2 "))
print(s.calculate(s=" 3+5 / 2 "))
print(s.calculate(s="0"))
