# Reverse Words in a String III
class Solution:
    def reverse(self, word):
        l = list(word)
        i, j = 0, len(l)-1
        while i < j:
            l[i], l[j] = l[j], l[i]
            i, j = i+1, j-1
        return ''.join(l)

    def reverseWords(self, s: str) -> str:
        res = [self.reverse(l) for l in s.split()]
        return ' '.join(res)


s = Solution()
print(s.reverseWords(s="Let's take LeetCode contest"))
print(s.reverseWords(s="God Ding"))
print(s.reverseWords(s="A"))
