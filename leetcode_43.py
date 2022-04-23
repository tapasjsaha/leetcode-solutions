# Multiply Strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convertToInt(s: str) -> int:
            total = 0
            for ch in s:
                total = total * 10 + (ord(ch) - ord('0'))
            return total

        return str(convertToInt(num1) * convertToInt(num2))


s = Solution()
print(s.multiply(num1="123", num2="456"))
print(s.multiply(num1="2", num2="3"))
