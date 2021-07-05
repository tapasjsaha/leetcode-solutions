#Uncommon Words from Two Sentences
class Solution:
    def uncommonFromSentences(self, s1, s2):
        d = {}
        for word in (s1 + ' ' + s2).split(' '):
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

        return [key for key, value in d.items() if value == 1]



s1 = Solution()
print(s1.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))
print(s1.uncommonFromSentences(s1 = "apple apple", s2 = "banana"))
print(s1.uncommonFromSentences(s1 = "a", s2 = "b"))
#print(s1.numberOfSteps(123))
