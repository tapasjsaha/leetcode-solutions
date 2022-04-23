# Longest Palindrome
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        max_len = 0
        for ch in s:
            if ch in d:
                del d[ch]
                max_len += 2
            else:
                d[ch] = 1

        max_len += 1 if bool(d) else 0

        return max_len


s = Solution()
print(s.longestPalindrome(s='abccccdd'))
print(s.longestPalindrome(s='a'))
print(s.longestPalindrome(s='dd'))
