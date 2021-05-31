def singleNonDuplicate(nums):
    nums.append('0')  # To take care of the scenario if the single number is at the end
    for j in range(0, len(nums), 2):
        if nums[j] != nums[j + 1]:
            break
    return int(nums[j])


def main():
    print("====================================================================")
    arr = input("Enter the array: ")
    nums = arr.split(',')
    y = singleNonDuplicate(nums)
    print(f"Single number is :{y}")


main()
