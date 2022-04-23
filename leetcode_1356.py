# Sort Integers by The Number of 1 Bits
class Solution:
    def sortByBits(self, arr: [int]) -> [int]:
        def numBits(n):
            count = 0
            while n:
                count += 1
                n = n & (n - 1)
            return count

        arr.sort(key=lambda x: (numBits(x), x))
        return arr


s = Solution()
print(s.sortByBits(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(s.sortByBits(arr=[1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))

