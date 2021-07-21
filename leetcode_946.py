# Validate Stack Sequences
class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        while pushed:
            pushed_top = pushed[0]
            popped_top = popped[0]
            if stack:
                stack_top = stack[-1]
            else:
                stack_top = None

            if pushed_top == popped_top:
                pushed.pop(0)
                popped.pop(0)
            elif stack_top == popped_top:
                popped.pop(0)
                stack.pop()
            else:
                a = pushed.pop(0)
                stack.append(a)

        stack.reverse()
        return stack == popped


s = Solution()
print(s.validateStackSequences(pushed=[], popped=[]))
print(s.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))
print(s.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))
print(s.validateStackSequences(pushed=[1], popped=[2]))
print(s.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[1, 2, 3, 4, 5]))
print(s.validateStackSequences(pushed=[1], popped=[1]))
print(s.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[5, 4, 3, 2, 1]))
print(s.validateStackSequences(pushed=[], popped=[]))
