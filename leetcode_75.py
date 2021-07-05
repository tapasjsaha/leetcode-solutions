class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        print(id(nums))
        red = []
        white = []
        blue = []
        for n in nums:
            if n == 0:
                red.append(n)
            elif n == 1:
                white.append(n)
            elif n == 2:
                blue.append(n)
            else:
                print(f"Received invalid option :{n}")
                exit()
        nums.clear()
        nums.extend(red + white + blue)
        print(id(nums))
        print(nums)
        return None


s = Solution()
s.sortColors([2, 0, 2, 1, 1, 0])
