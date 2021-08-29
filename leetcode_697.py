# Degree of an Array
class Solution:
    def findShortestSubArray(self, nums: [int]) -> int:
        d = {}
        maxOccr = 1
        for i, n in enumerate(nums):
            if n in d:
                d[n] = [d[n][0] + 1, d[n][1], i+1]
                if d[n][0] > maxOccr:
                    maxOccr = d[n][0]
            else:
                d[n] = [1, i+1, i+1]

        if maxOccr == 1:
            return 1
        else:
            res = [val for val in d.values() if val[0] == maxOccr]
            res.sort(key=lambda x: x[2]-x[1]+1)
            return res[0][2]-res[0][1]+1


s = Solution()
print(s.findShortestSubArray(nums=[1, 2, 2, 3, 1]))
print(s.findShortestSubArray(nums=[1, 2, 2, 3, 1, 4, 2]))
print(s.findShortestSubArray(nums=[0]))
