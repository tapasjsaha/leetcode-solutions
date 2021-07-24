# Longest Word in Dictionary through Deleting
class Solution:
    def findLongestWord(self, s: str, dictionary: list) -> str:
        valids = []
        ls = set(s)
        for word in dictionary:
            ld = set(word)
            if ld.issubset(ls):
                valids.append((word, len(word)))
        valids.sort(key=lambda x: (-x[1], x[0]))

        for word in valids:
            i, j = 0, 0
            while i < len(s) and j < len(word[0]):
                if s[i] == word[0][j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len(word[0]):
                return word[0]

        return ""


s = Solution()
print(s.findLongestWord(s="abpcplea", dictionary=["ale", "apple", "monkey", "plea", "aplpea"]))
print(s.findLongestWord(s="abpcplea", dictionary=["a", "b", "c"]))
print(s.findLongestWord(s="abpcplea", dictionary=["x", "y", "z"]))
