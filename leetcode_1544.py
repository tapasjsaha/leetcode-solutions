# Make The String Great
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if not stack:  # if stack is empty push the element
                stack.append(ch)
            elif (stack[-1].islower() and ch.isupper() and stack[-1] == ch.lower()) or (
                    stack[-1].isupper() and ch.islower() and stack[-1] == ch.upper()):
                # if stack not empty and cond match, remove both the charecter
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)


s = Solution()
print(s.makeGood(s="leEeetcode"))
print(s.makeGood(s="abBAcC"))
print(s.makeGood(s="s"))
