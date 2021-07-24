# Reverse String
class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i , j = 0, len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
 #       return None
        return s


s = Solution()
print(s.reverseString(s=["h", "e", "l", "l", "o"]))
print(s.reverseString(s=["H", "a", "n", "n", "a", "h"]))
