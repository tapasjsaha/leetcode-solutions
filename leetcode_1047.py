# Remove All Adjacent Duplicates In String
class Solution:
    def removeDuplicates(self, s: str) -> str:
        lst = []
        for ch in s:
            if lst and lst[-1] == ch:
                lst.pop()
            else:
                lst.append(ch)

        return "".join(lst)


s1 = Solution()
print(s1.removeDuplicates(s="abbaca"))
print(s1.removeDuplicates(s="azxxzy"))
print(s1.removeDuplicates(s=""))
print(s1.removeDuplicates(s="z"))
print(s1.removeDuplicates(s=" "))
