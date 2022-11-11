# Intersection of Two Arrays
class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        n1 = set(nums1)
        n2 = set(nums2)
        res = list(n1.intersection(n2))
        return res


s = Solution()
print(s.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(s.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
