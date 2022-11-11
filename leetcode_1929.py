# Concatenation of Array
class Solution:
    def getConcatenation(self, nums: [int]) -> [int]:
        ans = nums[:]
        ans.extend(nums)
        return ans


s = Solution()
print(s.getConcatenation(nums=[1, 2, 1]))
print(s.getConcatenation(nums=[1, 3, 2, 1]))

# JavaScript submission
"""
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let a = nums;
    a = a.concat(a);
    return a;    
};

"""