def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        if target - nums[i] in d:
            return [d[target - nums[i]], i]
        else:
            d[nums[i]] = i


#    for i in range(len(nums)):
#        if (target - nums[i]) in nums[i+1:]:
#            ind = nums[i+1:].index(target - nums[i]) + i + 1
#            break
#    return [i, ind]


def main():
    nums = [2,7,11,15] #[3,3] #[3,2,4]#[2,7,11,15]
    target = 9 #6 # 9
    print(f"{twoSum(nums, target)}")


main()