# Replace Elements with Greatest Element on Right Side
class Solution:
    def replaceElements(self, arr: [int]) -> [int]:
        m = max(arr)
        for ind, val in enumerate(arr[:-1]):
            if val == m:
                m = max(arr[ind+1:])
            arr[ind] = m
        arr[-1] = -1
        return arr


s = Solution()
print(s.replaceElements(arr=[17, 18, 5, 4, 6, 1]))
print(s.replaceElements(arr=[400]))
print(s.replaceElements(arr=[20, 18, 5, 4, 6, 1]))
print(s.replaceElements(arr=[20, 18, 5, 4, 6, 21]))
