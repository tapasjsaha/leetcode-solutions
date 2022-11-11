console.log("In console - leetcode_704.js")

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
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
return -1;
};

console.log(search(nums = [-1,0,3,5,9,12], target = 9));
console.log(search(nums = [-1,0,3,5,8,12], target = 9));
