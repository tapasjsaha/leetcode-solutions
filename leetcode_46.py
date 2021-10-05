# Permutations
class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        res = []
        if len(nums) == 1:
            return [nums[:]]
        else:
            for i in range(len(nums)):
                x = nums.pop(0)
                perms = self.permute(nums)
                for perm in perms:
                    perm.append(x)
                res.extend(perms)
                nums.append(x)
        return res


s = Solution()
print(s.permute([1, 2, 3, 4]))
