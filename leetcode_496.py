# Next Greater Element I
class Solution:
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        stack = []
        next_greater = {}
        for n in nums2[::-1]:
            while stack:
                if stack[-1] > n:
                    next_greater[n] = stack[-1]
                    break
                else:
                    stack.pop()
            stack.append(n)

        return [next_greater[i] if i in next_greater else -1 for i in nums1]


s = Solution()
print(s.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(s.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))

# This solution works but not optimized as for every element we need to traverse num2
# def nextGreat(num, indx):
#     for n in nums2[indx + 1:]:
#         if n > num:
#             return n
#     return -1
#
#
# res = []
# for n in nums1:
#     res.append(nextGreat(n, nums2.index(n)))
# return res
