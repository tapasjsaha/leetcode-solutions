# Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j, lw1, lw2 = 0, 0, len(word1), len(word2)
        res = ''
        while i < lw1 and j < lw2:
            res = res + word1[i] + word2[j]
            i += 1
            j += 1
        if word1[i:]:
            res += word1[i:]
        elif word2[j:]:
            res += word2[j:]
        return res


s = Solution()
print(s.mergeAlternately(word1="abc", word2="pqr"))
print(s.mergeAlternately(word1="ab", word2="pqrs"))
print(s.mergeAlternately(word1="abcd", word2="pq"))
print(s.mergeAlternately(word1="a", word2="pqrs"))
print(s.mergeAlternately(word1="abcd", word2="p"))
