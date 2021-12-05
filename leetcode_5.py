# Longest Palindromic Substring
# DP: https://www.youtube.com/watch?v=UflHuQj6MVA&t=484s
# Normal: https://www.youtube.com/watch?v=XYQecbcd6_c
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0
        for i in range(len(s)):
            # odd length palindrome
            start, end = i, i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end - start + 1 > res_len:
                    res_len = end - start + 1
                    res = s[start:end+1]
                start -= 1
                end += 1
            # even length palindrome
            start, end = i, i+1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end - start + 1 > res_len:
                    res_len = end - start + 1
                    res = s[start:end + 1]
                start -= 1
                end += 1
        return res


s = Solution()
print(s.longestPalindrome(s = "ababd"))
print(s.longestPalindrome(s = "abbd"))
