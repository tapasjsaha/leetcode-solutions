#Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        t = []
        words = s.split(' ')
        for i in range(len(words)-1, -1, -1):
            if words[i] != '':
                t.append(words[i])
        return ' '.join(t)


s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("  hello world  "))
