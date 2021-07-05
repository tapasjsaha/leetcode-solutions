# Count the Number of Consistent Strings
class Solution:
    def countConsistentStrings(self, allowed, words):
        cnt = 0
        s = set(allowed)
        for word in words:
            t = set(word)
            if t.issubset(s):
                cnt += 1
        return cnt


s1 = Solution()
print(s1.countConsistentStrings(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]))
print(s1.countConsistentStrings(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]))
print(s1.countConsistentStrings(allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]))
