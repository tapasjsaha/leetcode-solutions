# Add Strings
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res, carry = [], 0
        mlen = max(len(num1), len(num2))
        num1 = num1[::-1].ljust(mlen, '0')
        num2 = num2[::-1].ljust(mlen, '0')
        for i in range(mlen):
            s = carry + ord(num1[i]) + ord(num2[i]) - 2 * ord('0')
            res.append(str(s % 10))
            carry = s//10
        if carry != 0:
            res.append(str(carry))
        return ''.join(res[::-1])


s = Solution()
print(s.addStrings(num1="12", num2="123"))
print(s.addStrings(num1="9998", num2="3"))
