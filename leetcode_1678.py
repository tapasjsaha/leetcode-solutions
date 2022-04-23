# Goal Parser Interpretation
class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        res = ''
        while i < len(command):
            if command[i] == 'G':
                res += 'G'
            elif command[i] == '(':
                pass
            elif command[i] == ')':
                res += 'o'
            elif command[i] == 'a':
                res += 'al'
                i += 2
            i += 1
        return res


s = Solution()
print(s.interpret(command="G()(al)"))
print(s.interpret(command="G()()()()(al)"))
print(s.interpret(command="(al)G(al)()()G"))
