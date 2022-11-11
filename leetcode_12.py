# Integer to Roman
class Solution:
    def intToRoman(self, num: int) -> str:
        from collections import OrderedDict
        d = OrderedDict(
            {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
             4: 'IV', 1: 'I'})
        ans = ""
        for key, value in d.items():
            while num >= key:
                num -= key
                ans = ans + value
            if num == 0:
                break

        return ans


s = Solution()
print(s.intToRoman(num=3))
print(s.intToRoman(num=58))
print(s.intToRoman(num=1994))

# dict = {
#     1: 'I',
#     4: 'IV',
#     5: 'V',
#     9: 'IX',
#     10: 'X',
#     40: 'XL',
#     50: 'L',
#     90: 'XC',
#     100: 'C',
#     400: 'CD',
#     500: 'D',
#     900: 'CM',
#     1000: 'M'
# }
#
# min_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#
#
# def convertRoman(num):
#     y = ''
#     while num != 0:
#         for i in range(len(min_list)):
#             if num - min_list[i] >= 0:
#                 y = y + dict[min_list[i]]
#                 num -= min_list[i]
#                 break
#             else:
#                 continue
#     return y
#
#
# def main():
#     print("====================================================================")
#     while True:
#         inp = input("Enter Number: ")
#         if inp.isdigit():
#             x = int(inp)
#             y = convertRoman(x)
#             print(f"Corresponding Roman number is :{y}")
#         else:
#             break
#
#
# main()
