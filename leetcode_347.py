# Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums, k):
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        # ls = sorted([(x, y) for x, y in d.items()], key= lambda x : x[1], reverse= True)
        res = [x for x, y in sorted([(x, y) for x, y in d.items()], key=lambda x: x[1], reverse=True)]
        return res[:k]


s1 = Solution()
print(s1.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
print(s1.topKFrequent(nums=[1], k=1))
print(s1.topKFrequent(nums=[1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4], k=2))
