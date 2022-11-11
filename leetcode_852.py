class Solution:
    def peakIndexInMountainArray(self, arr: [int]) -> int:
        low, left, high, right = 0, 0, len(arr) - 1, len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if mid > left and arr[mid - 1] > arr[mid]:
                high = mid - 1
            elif mid < right and arr[mid + 1] > arr[mid]:
                low = mid + 1
            else:
                return mid
        return low


s = Solution()
print(s.peakIndexInMountainArray(arr=[0, 1, 0]))
print(s.peakIndexInMountainArray(arr=[0, 2, 1, 0]))
print(s.peakIndexInMountainArray(arr=[0, 10, 5, 2]))

print(s.peakIndexInMountainArray(arr=[10, 9, 8, 7]))
print(s.peakIndexInMountainArray(arr=[10, 11, 12, 13, 14]))

print(s.peakIndexInMountainArray(arr=[3, 9, 8, 6, 4]))
