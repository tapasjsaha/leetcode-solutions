console.log("In console - leetcode_35.js")

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
var low = 0, high = nums.length-1;
while (low <= high){
    mid = (low+high)//2
        if (nums[mid] == target)
            return mid
        else if (nums[mid] > target)
            high = mid - 1
        else
            low = mid + 1
		}

if (nums[mid] > target)
    return mid
else
    return (mid+1)
};


console.log(searchInsert(nums = [1,3,5,6], target = 5));
console.log(searchInsert(nums = [1,3,5,6], target = 2));
console.log(searchInsert(nums = [1,3,5,6], target = 7));
