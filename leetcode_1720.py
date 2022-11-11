# Decode XORed Array
class Solution:
    def decode(self, encoded: [int], first: int) -> [int]:
        res = [first]
        for a in encoded:
            res.append(a ^ res[-1])
        return res


s = Solution()
print(s.decode(encoded=[1, 2, 3], first=1))
print(s.decode(encoded=[6, 2, 7, 3], first=4))
