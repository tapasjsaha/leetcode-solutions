# Delete Characters to Make Fancy String
class Solution:
    def makeFancyString(self, s: str) -> str:
        stack, count = [], 0
        for ch in s:
            if stack:
                if stack[-1] == ch and count == 2:
                    pass
                elif stack[-1] == ch and count == 1:
                    stack.append(ch)
                    count += 1
                else:
                    stack.append(ch)
                    count = 1
            else:
                stack.append(ch)
                count += 1
        return ''.join(stack)


s = Solution()
print(s.makeFancyString(s="leeetcode"))
print(s.makeFancyString(s="aaabaaaa"))
print(s.makeFancyString(s="aab"))
