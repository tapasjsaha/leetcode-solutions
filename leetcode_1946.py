# Largest Number After Mutating Substring
class Solution:
    def maximumNumber(self, num: str, change: [int]) -> str:
        lst = [int(n) for n in num]
        i, flag = 0, -1
        while i < len(lst) and flag < 1:
            if lst[i] < change[lst[i]]:
                lst[i] = change[lst[i]]
                if flag == -1:
                    flag = 0
            elif flag == 0:
                if lst[i] > change[lst[i]]:
                    flag = 1
            else:
                pass
            i += 1

        ch = [str(c) for c in lst]
        return ''.join(ch)


s = Solution()
print(s.maximumNumber(num="132", change=[9, 8, 5, 0, 3, 6, 4, 2, 6, 8]))
print(s.maximumNumber(num="021", change=[9, 4, 3, 5, 7, 2, 1, 9, 0, 6]))
print(s.maximumNumber(num="5", change=[1, 4, 7, 5, 3, 2, 5, 6, 9, 4]))
print(s.maximumNumber(num="991", change=[9, 8, 5, 0, 3, 6, 4, 2, 6, 8]))
print(s.maximumNumber(num="214010", change=[6, 7, 9, 7, 4, 0, 3, 4, 4, 7]))

