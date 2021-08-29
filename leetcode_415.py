# Add Strings
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        res, just = 0, max(len(num1), len(num2))
        num1, num2 = num1.rjust(just, '0'), num2.rjust(just, '0')
        for i in range(just):
            res *= 10
            res = res + dic[num1[i]] + dic[num2[i]]
        return str(res)


s = Solution()
print(s.addStrings(num1="11", num2="123"))
print(s.addStrings(num1="456", num2="77"))
print(s.addStrings(num1="0", num2="0"))
print(s.addStrings(num1="0", num2="12345"))
