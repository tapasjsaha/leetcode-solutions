# Count Hills and Valleys in an Array
class Solution:
    def countHillValley(self, nums: [int]) -> int:
        prev = nums[0]
        inp = [prev]
        for n in nums[1:]:
            if n != prev:
                inp.append(n)
                prev = n

        count = 0
        for i in range(1, len(inp)-1, 1):
            if (inp[i] > inp[i-1] and inp[i] > inp[i+1]) or (inp[i] < inp[i-1] and inp[i] < inp[i+1]):
                count += 1

        return count


s = Solution()
print(s.countHillValley(nums=[2, 4, 1, 1, 6, 5]))
print(s.countHillValley(nums=[6, 6, 5, 5, 4, 1]))



#
# # Javascript Solution :
#
# / **
# * @ param
# {number[]}
# nums
# * @ return {number}
# * /
# var
# countHillValley = function(nums)
# {
#     let
# inp = [nums[0]];
# for (let i=1; i < nums.length; i++)
# {
# if (nums[i] != nums[i - 1])
# {
#     inp.push(nums[i]);
# }}
#
# var
# count = 0;
# for (let j=1; j < inp.length - 1; j++)
# {
# if ((inp[j] > inp[j - 1] & & inp[j] > inp[j + 1]) | | (inp[j] < inp[j - 1] & & inp[j] < inp[j + 1]))
# {
#     count = count + 1;
# }}
#
# return count;
# };