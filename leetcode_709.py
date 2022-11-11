# To Lower Case
class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ''
        for ch in s:
            if ord('Z') >= ord(ch) >= ord('A'):
                res += chr(ord(ch) ^ (1 << 5))
            else:
                res += ch
        return res


s = Solution()
print(s.toLowerCase(s="Hello"))
print(s.toLowerCase(s="here"))
print(s.toLowerCase(s="LOVELY"))


# def toLowerCase(s):
#     res = ''
#     for ch in s:
#         if 65 <= ord(ch) <= 90:
#             res += chr(ord(ch) + 32)
#         else:
#             res += ch
#     return res
#
#
# def main():
#     in_str = input("Enter string: ")
#     out_str = toLowerCase(in_str)
#     print(f"Output String: {out_str}")
#
#
# main()
