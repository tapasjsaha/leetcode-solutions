# Kth Largest Element in an Array

class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        ne = len(nums)
        for i in range(ne // 2, -1, -1):
            self.heapify(nums, ne, i)

        item = nums[0]
        for j in range(k-1):
            nums[0]=nums[ne-1]
            ne -= 1
            self.heapify(nums, ne, 0)
            item = nums[0]

        return item

    def heapify(self, nums, ne, start):
        """self - array or heap,
        ne - total number of elements in the heap,
        start - is the starting index"""
        greatest = start
        left = (2 * (start + 1)) - 1  # left = 2i in 1 index
        right = (2 * (start + 1)) + 1 - 1  # right = 2i+1 in 1 index
        if left < ne and nums[left] > nums[greatest]:
            greatest = left
        if right < ne and nums[right] > nums[greatest]:
            greatest = right
        if greatest != start:
            nums[greatest], nums[start] = nums[start], nums[greatest]
            self.heapify(nums, ne, greatest)


s = Solution()
print(s.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))

print(s.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
