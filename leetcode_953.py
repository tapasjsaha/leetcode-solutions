# Verifying an Alien Dictionary
class Solution:
    def isAlienSorted(self, words: [str], order: str) -> bool:
        l1 = list(order)
        l2 = list('abcdefghijklmnopqrstuvwxyz')
        d = dict(zip(l1, l2))

        def helper(word):
            res = ''
            for ch in word:
                res += d[ch]
            return res

        converted_words = [helper(word) for word in words]
        originals = converted_words[:]
        converted_words.sort()
        return originals == converted_words


s = Solution()
print(s.isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
print(s.isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"))
print(s.isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"))
