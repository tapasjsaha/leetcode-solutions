# Check If Two String Arrays are Equivalent
class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        return "".join(word1) == "".join(word2)


s1 = Solution()

print(s1.arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]))
print(s1.arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]))
print(s1.arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"]))
print(s1.arrayStringsAreEqual(word1=[" ", " ", " "], word2=["  ", " "]))
print(s1.arrayStringsAreEqual(word1=[""], word2=[" "]))
