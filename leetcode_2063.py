# Vowels of All Substrings
class Solution:
    def countVowels(self, word: str) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        res = 0
        n = len(word)
        for i in range(n):
            if word[i] in vowel:
                res = res + ((n - i) * (i + 1))
        return res


s = Solution()
print(s.countVowels(word="aba"))
print(s.countVowels(word="abc"))
print(s.countVowels(word="ltcd"))
