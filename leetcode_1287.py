# Element Appearing More Than 25% In Sorted Array
class Solution:
    def findSpecialInteger(self, arr):
        l = len(arr)
        req = l // 4
        if l <= 4:
            for i in set(arr):
                if arr.count(i) > req:
                    return i
        else:
            for i in [0, l // 4, l // 2, (3 * l) // 4, l - 1]:
                if arr.count(arr[i]) > req:
                    return arr[i]
        return None


s1 = Solution()

print(s1.findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]))
print(s1.findSpecialInteger(arr=[1, 1]))
print(s1.findSpecialInteger(arr=[0]))
