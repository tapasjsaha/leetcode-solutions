# Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        res = []
        d = {}
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        for n in nums1:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        for m in nums2:
            if m in d and d[m] > 0:
                res.append(m)
                d[m] -= 1
        return res


s = Solution()
print(s.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(s.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
print(s.intersect(nums1=[1, 2], nums2=[9, 4]))
print(s.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2, 2, 2]))
