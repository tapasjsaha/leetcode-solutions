# Number of Good Pairs
class Solution:
    def numIdenticalPairs(self, nums: [int]) -> int:
        d = {}
        cnt = 0
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        for v in d.values():
            if v > 1:
                cnt += v*(v-1)//2
        return cnt


s = Solution()
print(s.numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]))
print(s.numIdenticalPairs(nums=[1, 1, 1, 1]))
print(s.numIdenticalPairs(nums=[1, 2, 3]))
