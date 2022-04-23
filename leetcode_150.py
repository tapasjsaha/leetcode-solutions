# Evaluate Reverse Polish Notation
class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        result_stack = []
        for token in tokens:
            if token in '+-*/':
                op2 = int(result_stack.pop())
                op1 = int(result_stack.pop())
                if token == '+':
                    result = op1 + op2
                elif token == '-':
                    result = op1 - op2
                elif token == '*':
                    result = op1 * op2
                elif token == '/':
                    result = int(op1/op2)
                result_stack.append(result)
            else:
                result_stack.append(token)
        return result_stack[0]


s = Solution()
print(s.evalRPN(tokens=["2", "1", "+", "3", "*"]))
print(s.evalRPN(tokens=["4", "13", "5", "/", "+"]))
print(s.evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(s.evalRPN(tokens=["2"]))

# Accepted solution 22%
# from fractions import Fraction
# class Solution:
#     def evalRPN(self, tokens: [str]) -> int:
#         result_stack = []
#         op = ['+', '-', '*', '/']
#         for token in tokens:
#             if token in op:
#                 op2 = int(result_stack.pop())
#                 op1 = int(result_stack.pop())
#                 if token == '+':
#                     result = op1 + op2
#                 elif token == '-':
#                     result = op1 - op2
#                 elif token == '*':
#                     result = op1 * op2
#                 elif token == '/':
#                     result = int(Fraction(op1, op2))
#                 result_stack.append(result)
#             else:
#                 result_stack.append(token)
#         return result_stack[0]