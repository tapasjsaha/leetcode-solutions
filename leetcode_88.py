# Merge Sorted Array
class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m -= 1
        n -= 1
        curr = len(nums1) - 1
        while n >= 0 and m >= 0:
            if nums1[m] <= nums2[n]:
                nums1[curr] = nums2[n]
                curr -= 1
                n -= 1
            else:
                nums1[curr] = nums1[m]
                curr -= 1
                m -= 1
        if m < 0:
            nums1[:n+1] = nums2[:n+1]
        print("------------------------")
        print(nums1)
        return None

    #    import array as arr
    #    arr_nums1 = arr.array('i', nums1)
    #    arr_nums2 = arr.array('i', nums2)
    #    print(arr_nums1)
    #    print(arr_nums2)
    #    m -= 1
    #    n -= 1
    #    curr = len(nums1)-1
    #    while n >= 0:
    #        if arr_nums1[m] <= arr_nums2[n]:
    #            arr_nums1[curr] = arr_nums2[n]
    #            curr -= 1
    #            n -= 1
    #        else:
    #            arr_nums1[curr] = arr_nums1[m]
    #            curr -= 1
    #            m -= 1
    #    print("------------------------")
    #    print(arr_nums1)
    #    return None


s = Solution()
print(s.merge([1, 4, 6, 0, 0, 0], 3, [2, 3, 5], 3))

print(s.merge([2, 0], 1, [1], 1))
