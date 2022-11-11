# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
class Solution:
    def numOfSubarrays(self, arr: [int], k: int, threshold: int) -> int:
        # implemented using sliding window technique O(N)
        sm, res = 0, 0
        for i in range(k):
            sm += arr[i]
        if sm / k >= threshold:
            res += 1

        for i in range(k, len(arr)):
            sm = sm + arr[i] - arr[i - k]
            if sm / k >= threshold:
                res += 1

        return res


s1 = Solution()
print(s1.numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4))
print(s1.numOfSubarrays(arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5))
