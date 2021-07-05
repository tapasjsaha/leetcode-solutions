#Top K Frequent Words
class Solution:
    def topKFrequent(self, words, k):
        res = []
        dwords = {}
        for word in words:
            if word in dwords:
                dwords[word] += 1
            else:
                dwords[word] = 1
        print(dwords)
        l = list(set(dwords.values()))
        l.sort(reverse=True)
        for i in l:
            lst = []
            for ky, v in dwords.items():
                if v == i:
                    lst.append(ky)
            lst.sort()
            res.extend(lst)
        return res[:k]




s1 = Solution()
print(s1.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is", "may"], 4))
print(s1.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))