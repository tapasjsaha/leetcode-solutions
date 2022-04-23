class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif not haystack:
            return -1
        else:
            i, l = 0, len(needle)
            while (i+l-1) < len(haystack):
                if haystack[i:i+l] == needle:
                    return i
                i += 1
            return -1

# Accepted solution but no algorithm (using in built function)
#         try:
#             res = haystack.index(needle)
#             return res
#         except ValueError:
#             return -1

s = Solution()
print(s.strStr(haystack="hello", needle="ll"))
print(s.strStr(haystack="aaaaa", needle="bba"))
print(s.strStr(haystack="", needle=""))
print(s.strStr(haystack="abcd", needle=""))
print(s.strStr(haystack="", needle="abc"))
