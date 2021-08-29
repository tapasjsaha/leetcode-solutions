# Last Stone Weight
import bisect


class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        import bisect
        stones.sort()
        while len(stones) > 1:
            x, y = stones[-1], stones[-2]
            stones = stones[:-2]
            if abs(x-y) > 0:
                bisect.insort_right(stones, abs(x - y))
        return stones[0] if stones else 0


s = Solution()
print(s.lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]))
print(s.lastStoneWeight(stones=[1]))
print(s.lastStoneWeight(stones=[1, 1, 2, 3, 5]))
