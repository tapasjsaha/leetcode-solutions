# Remove Invalid Parentheses
class Solution:
    def removeInvalidParentheses(self, s: str) -> [str]:

        def isValid(st: str):
            stack = []
            for ch in st:
                if ch == '(':
                    stack.append(ch)
                elif ch == ')':
                    try:
                        stack.pop()
                    except IndexError:
                        return False
                else:
                    pass
            return True if not stack else False

        def checkInvalidParantheses(st: str):
            left = 0
            right = 0
            for ch in st:
                if ch == '(':
                    left += 1
                elif ch == ')':
                    if left > 0:
                        left -= 1
                    else:
                        right += 1
                else:
                    pass
            return left, right

        def backtrack(current, invalid_left, invalid_right, currPos, left, right):
            if invalid_left == 0 and invalid_right == 0 and currPos == len(s):
                if isValid(current[:]):
                    res_set.add(current[:])
                else :
                    print("Hi:"+current[:])
            elif (invalid_left > 0 or invalid_right > 0) and currPos == len(s):
                return
            else:
                if s[currPos] == '(' and invalid_left > 0:
                    candidate_list = ['', '(']
                    for candidate in candidate_list:
                        backtrack(current + candidate, invalid_left + len(candidate) - 1, invalid_right, currPos+1, left + len(candidate), right)
                elif s[currPos] == ')' and invalid_right > 0:
                    candidate_list = ['']
                    if left > right:
                        candidate_list.append(')')
                    for candidate in candidate_list:
                        backtrack(current + candidate, invalid_left, invalid_right + len(candidate) - 1, currPos+1, left, right + len(candidate))
                elif s[currPos] == '(':
                    backtrack(current + s[currPos], invalid_left, invalid_right, currPos+1, left+1, right)
                elif s[currPos] == ')':
                    backtrack(current + s[currPos], invalid_left, invalid_right, currPos + 1, left, right+1)
                else:
                    backtrack(current + s[currPos], invalid_left, invalid_right, currPos + 1, left, right)

        res_set = set()
        invalid_left, invalid_right = checkInvalidParantheses(s)
        backtrack('', invalid_left, invalid_right, 0, 0, 0)

        return list(res_set)


s = Solution()
print(s.removeInvalidParentheses('(anabd)'))

print(s.removeInvalidParentheses(')()('))


print(s.removeInvalidParentheses(s="()())()"))
print(s.removeInvalidParentheses(s="(a)())()"))
print(s.removeInvalidParentheses(s=")("))
print(s.removeInvalidParentheses(s="))))))))))))))))))))aaaaa"))
