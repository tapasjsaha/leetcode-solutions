# Ambiguous Coordinates

# If the slice is '0', then return ['0']
# If the slice starts and ends with '0', we generate nothing. Because we cannot have 0.****0
# If the slice starts with '0', then the only number we generate is 0.****
# If the slice does not start with '0', but ends with '0', which means we can only generate *****0 without decimal
#  point. Otherwise, we'd end up with ***.***0
# If the slice does not start with or end with '0', then we can generate lots of numbers by inserting the decimal
#  points at any position. For example, using ABCD as a base, then we can generate A.BCD, AB.CD, ABC.D.

class Solution:
    def ambiguousCoordinates(self, s: str) -> [str]:
        res = []
        s = s[1:-1]

        def possible_coordinate(x):
            if x == '0':
                return ['0']
            elif x.startswith('0') and x.endswith('0'):
                return []
            elif x.startswith('0'):
                return ['0.'+x[1:]]
            elif x.endswith('0'):
                return [x]
            else:
                temp = [x[:i]+'.'+x[i:] for i in range(1, len(x))]
                temp.append(x)
                return temp

        def findSol(first, second):
            possible_first_coordinates = possible_coordinate(first)
            possible_second_coordinates = possible_coordinate(second)
            if not possible_first_coordinates or not possible_second_coordinates:
                pass
            else:
                for fst in possible_first_coordinates:
                    for snd in possible_second_coordinates:
                        res.append('('+fst+', '+snd+')')

        for i in range(1, len(s)):
            findSol(s[:i], s[i:])

        return res


s = Solution()
print(s.ambiguousCoordinates(s="(123)"))
print(s.ambiguousCoordinates(s="(0000)"))
print(s.ambiguousCoordinates(s="(0001)"))
print(s.ambiguousCoordinates(s="(1000)"))
print(s.ambiguousCoordinates(s="(10010)"))
