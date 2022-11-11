# Compare Strings by Frequency of the Smallest Character
class Solution:
    def numSmallerByFrequency(self, queries: [str], words: [str]) -> [int]:
        # function to determine frequency of lexicographically smallest charecter
        def f(s):
            lst = list(s)
            lst.sort()
            return lst.count(lst[0])

        # count of f(word), maintaining array of size 10 as 1 <= queries[i].length, words[i].length <= 10
        count_words = [0] * 11
        for word in words:
            count_words[f(word)] += 1
        count_words.append(0)

        # creating prefix array with counts
        for i in range(10, -1, -1):
            count_words[i] = count_words[i] + count_words[i + 1]

        # answering each query
        output = []
        for query in queries:
            l = f(query)
            output.append(count_words[l + 1])

        return output


s1 = Solution()
print(s1.numSmallerByFrequency(queries=["cbd"], words=["zaaaz"]))
print(s1.numSmallerByFrequency(queries=["bbb", "cc"], words=["a", "aa", "aaa", "aaaa"]))
