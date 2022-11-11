# Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:

        def lessThanK(ar, k):
            l, h = 0, len(ar) - 1
            ans = 0
            while l <= h:
                mid = l + (h - l) // 2
                if ar[mid] < k:
                    ans = mid + 1
                    l = mid + 1
                else:
                    h = mid - 1
            return ans

        def posElim(n):
            if len(nums1) == 0:
                low, high = nums2[0], nums2[-1]
            elif len(nums2) == 0:
                low, high = nums1[0], nums1[-1]
            else:
                low, high = min(nums1[0], nums2[0]), max(nums1[-1], nums2[-1])
            ans = 0
            while low <= high:
                mid = low + (high - low) // 2
                if len(nums1) == 0:
                    x = 0
                else:
                    x = lessThanK(nums1, mid)
                if len(nums2) == 0:
                    y = 0
                else:
                    y = lessThanK(nums2, mid)
                if x + y <= n:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        l = len(nums1) + len(nums2)
        if l % 2 == 0:
            m1 = posElim(l // 2)
            m2 = posElim(l // 2 - 1)
            return (m1 + m2) / 2
        else:
            m = posElim(l // 2)
            return m


s = Solution()
print(s.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
print(s.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
