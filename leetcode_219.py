# Contains Duplicate II
class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        if k == 0:
            return False
        i, j = 0, 0
        d = {}
        while j < k and j < len(nums):
            if nums[j] in d:
                d[nums[j]] += 1
            else:
                d[nums[j]] = 1
            j += 1

        for val in d.values():
            if val > 1:
                return True

        while j < len(nums):
            if nums[j] in d:
                return True
            else:
                d[nums[j]] = 1
                j += 1
                if d[nums[i]] == 1:
                    del d[nums[i]]
                else:
                    d[nums[i]] -= 1
                i += 1
        return False


s = Solution()
print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
print(s.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))
print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
