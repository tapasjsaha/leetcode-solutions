# Count Common Words With One Occurrence
class Solution:
    def countWords(self, words1: [str], words2: [str]) -> int:
        dwords1, dwords2 = {}, {}
        for word in words1:
            dwords1[word] = 1 + dwords1.get(word, 0)
        for word in words2:
            dwords2[word] = 1 + dwords2.get(word, 0)

        count = 0
        for key, val in dwords1.items():
            if val == 1 and dwords2.get(key, 0) == 1:
                count += 1

        return count


s1 = Solution()
print(s1.countWords(words1=["leetcode", "is", "amazing", "as", "is"], words2=["amazing", "leetcode", "is"]))
print(s1.countWords(words1=["b", "bb", "bbb"], words2=["a", "aa", "aaa"]))
print(s1.countWords(words1=["a", "ab"], words2=["a", "a", "a", "ab"]))
