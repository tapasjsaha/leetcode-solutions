# Reverse Vowels of a String
class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s = list(s)
        low, high = 0, n - 1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        while low < high:
            while low < n and s[low] not in vowels:
                low += 1
            while high >= 0 and s[high] not in vowels:
                high -= 1
            if low < high:
                s[low], s[high] = s[high], s[low]
                low += 1
                high -= 1

        return ''.join(s)



# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         n = len(s)
#         i, j = 0, n - 1
#         lst = list(s)
#         vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#         while True:
#             while i < n and lst[i] not in vowel:
#                 i += 1
#             while j >= 0 and lst[j] not in vowel:
#                 j -= 1
#             if i < j:
#                 lst[i], lst[j] = lst[j], lst[i]
#                 i += 1
#                 j -= 1
#             else:
#                 break
#         return ''.join(lst)


s = Solution()
print(s.reverseVowels(s='hello'))
print(s.reverseVowels(s='leutcodi'))
print(s.reverseVowels(s='bad'))
print(s.reverseVowels(s='aeiou'))
print(s.reverseVowels(s='bcdfgh'))
