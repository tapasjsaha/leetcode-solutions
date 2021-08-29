# Kth Missing Positive Number
class Solution:
    def findKthPositive(self, arr: [int], k: int) -> int:
        c = 0
        for i in range(1, arr[-1] + k + 1):
            if i not in arr:
                c += 1
                if c == k:
                    return i


s = Solution()
print(s.findKthPositive(arr=[2, 3, 4, 7, 11], k=5))
print(s.findKthPositive(arr=[1, 2, 3, 4], k=2))
