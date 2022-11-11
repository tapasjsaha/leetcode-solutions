# Set Mismatch --- tle
class Solution:
    def findErrorNums(self, nums: [int]) -> [int]:
        # TC : O(N), SC: O(1) solution using bit-manipulation
        n = len(nums)
        bit_xor = 0
        for num in nums:
            bit_xor ^= num
        for i in range(n):
            bit_xor ^= (i + 1)
        # bit_xor now holds the value of missing number xor duplicate number

        # check the setbit of bit_xor
        b = 0
        while (bit_xor >> b) & 1 != 1:
            b += 1

        num1, num2 = 0, 0
        for num in nums:
            if (num >> b) & 1 == 0:
                num1 ^= num
            else:
                num2 ^= num
        for i in range(1, n + 1, 1):
            if (i >> b) & 1 == 0:
                num1 ^= i
            else:
                num2 ^= i

        if num1 in nums:
            return [num1, num2]
        else:
            return [num2, num1]


# # TC : O(N), SC: O(N) solution as set is created
# class Solution:
#     def findErrorNums(self, nums: [int]) -> [int]:
#         # # TC : O(N), SC: O(N) solution as set is created
#         n = len(nums)
#         actual_sum = n * (n+1) // 2
#         current_sum = sum(nums)
#         set_sum = sum(set(nums))
#         return [current_sum - set_sum, actual_sum - set_sum]


s = Solution()
print(s.findErrorNums(nums=[1, 2, 2, 4]))
print(s.findErrorNums(nums=[1, 1]))
print(s.findErrorNums(nums=[2, 2]))

# Correct but not in time limit as it is a O(N^2) solution
#    def findErrorNums(self, nums: [int]) -> [int]:
#        found = 0
#        for ch in range(1, len(nums)+1):
#            if nums.count(ch) == 2:
#                x = ch
#                found += 1
#            if ch not in nums:
#                y = ch
#                found += 1
#            if found == 2:
#                break
#        return [x, y]



