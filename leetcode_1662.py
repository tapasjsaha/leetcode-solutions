# Check If Two String Arrays are Equivalent
class Solution:
    def arrayStringsAreEqual(self, word1: [str], word2: [str]) -> bool:
        # TC is O(N), SC is O(1) as we are checking char by char
        ch1, wd1, ch2, wd2 = 0, 0, 0, 0
        while wd1 < len(word1) and wd2 < len(word2):
            if word1[wd1][ch1] != word2[wd2][ch2]:
                return False
            ch1 += 1
            ch2 += 1
            if ch1 >= len(word1[wd1]):
                ch1 = 0
                wd1 += 1
            if ch2 >= len(word2[wd2]):
                ch2 = 0
                wd2 += 1

        if wd1 == len(word1) and wd2 == len(word2):
            return True
        else:
            return False


# Valid solution, but SC is O(N)
# class Solution:
#     def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
#         return "".join(word1) == "".join(word2)


s1 = Solution()
print(s1.arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]))
print(s1.arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]))
print(s1.arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"]))

"""Not a valid test case as constraints are 1 <= word1.length, word2.length <= 103 
and word1[i] and word2[i] consist of lowercase letters"""
# print(s1.arrayStringsAreEqual(word1=[" ", " ", " "], word2=["  ", " "]))
# print(s1.arrayStringsAreEqual(word1=[""], word2=[" "]))
