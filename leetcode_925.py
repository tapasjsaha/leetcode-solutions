# Long Pressed Name
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed:
            return True
        if len(name) > len(typed):
            return False
        if set(name) != set(typed):
            return False

        i, j = 0, 0
        name_stack = []
        typed_stack = []
        while i < (len(name)) and j < (len(typed)):
            if typed[j] == name[i]:
                name_stack.append(name[i])
                typed_stack.append(typed[j])
                i += 1
            elif name_stack and typed[j] == name_stack[-1]:
                pass
            else:
                return False
            j += 1

        if j < (len(typed)):
            while j < (len(typed)):
                if typed[j] == name_stack[-1]:
                    pass
                else:
                    typed_stack.append(typed[j])
                j += 1

        return list(name) == name_stack and name_stack == typed_stack


s = Solution()
print(s.isLongPressedName(name="pyplrz", typed="ppyypllr"))
print(s.isLongPressedName(name="alexd", typed="ale"))
print(s.isLongPressedName(name="vtkgn", typed="vttkgnn"))
print(s.isLongPressedName(name="alex", typed="aaleex"))
print(s.isLongPressedName(name="saeed", typed="ssaaedd"))
print(s.isLongPressedName(name="leelee", typed="lleeelee"))
print(s.isLongPressedName(name="laiden", typed="laiden"))


