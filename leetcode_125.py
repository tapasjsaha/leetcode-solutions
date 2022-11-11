# Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for ch in s:
            if ch.isalnum():
                if ch.isalpha():
                    res = res + ch.lower()
                else:
                    res = res + ch
        rev = res[::-1]
        return res == rev


s = Solution()
print(s.isPalindrome(s="A man, a plan, a canal: Panama"))
print(s.isPalindrome(s="race a car"))
print(s.isPalindrome(s=" "))
print(s.isPalindrome(s="0P"))
