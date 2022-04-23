# Increasing Triplet Subsequence
class Solution:
    def increasingTriplet(self, nums: [int]) -> bool:
        i, j = float('inf'), float('inf')
        for n in nums:
            if n < i:
                i = n
            elif i < n < j:
                j = n
            elif j < n < float('inf'):
                return True
        return False


s = Solution()
print(s.increasingTriplet(nums=[0, 4, 2, 1, 0, -1, -3]))
print(s.increasingTriplet(nums=[1, 2, 3, 4, 5]))
print(s.increasingTriplet(nums=[5, 4, 3, 2, 1]))
print(s.increasingTriplet(nums=[2, 1, 5, 0, 4, 6]))
