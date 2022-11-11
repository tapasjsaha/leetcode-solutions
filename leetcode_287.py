# Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        # O(NlogN) solution using Bianary Search
        def countLessEq(x):
            cnt = 0
            for n in nums:
                if n <= x:
                    cnt += 1
            return cnt

        low, high = 1, len(nums)
        dup = 0
        while low <= high:
            mid = low + (high - low) // 2
            x = countLessEq(mid)
            if x <= mid:
                low = mid + 1
            elif x > mid:
                dup = mid
                high = mid - 1
        return dup


# nums = [2,2,2,2,2] is a testcase, hence difficult to solve with bit manupulation
s = Solution()
print(s.findDuplicate(nums=[1, 3, 4, 2, 2]))
print(s.findDuplicate(nums=[3, 1, 3, 4, 2]))
print(s.findDuplicate(nums=[2, 2, 2, 2, 2]))
