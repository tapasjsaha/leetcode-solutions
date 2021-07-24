# Plus One
class Solution:
    def plusOne(self, digits: list) -> list:
        digits.insert(0, 0)
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] <= 9:
                break
            else:
                digits[i] = 0
        if digits[0] == 0:
            digits.pop(0)
        return digits


s = Solution()
print(s.plusOne(digits=[1, 2, 3]))
print(s.plusOne(digits=[4, 3, 2, 1]))
print(s.plusOne(digits=[0]))
print(s.plusOne(digits=[1, 9, 9]))
print(s.plusOne(digits=[9, 9, 9]))
