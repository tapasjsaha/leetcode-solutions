# 1-bit and 2-bit Characters
class Solution:
    def isOneBitCharacter(self, bits: list) -> bool:
        counter, i = 0, 0
        while i < len(bits):
            if bits[i] == 0:
                i += 1
                counter = 1
            else:
                i += 2
                counter = 2
        return counter == 1


s = Solution()
print(s.isOneBitCharacter(bits=[1, 0, 0]))
print(s.isOneBitCharacter(bits=[1, 1, 1, 0]))
print(s.isOneBitCharacter(bits=[1, 1, 0, 0, 0, 1, 0]))
print(s.isOneBitCharacter(bits=[0]))
