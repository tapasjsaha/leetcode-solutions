# Range Sum Query - Immutable
class NumArray:

    def __init__(self, nums: [int]):
        self.nums = nums
        self.prefixSum = []
        sumSofar = 0
        for n in nums:
            sumSofar += n
            self.prefixSum.append(sumSofar)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            pre = 0
        else:
            pre = self.prefixSum[left - 1]
        post = self.prefixSum[right]
        return post - pre


# Your NumArray object will be instantiated and called as such:
obj = NumArray(nums=[-2, 0, 3, -5, 2, -1])
print(obj.sumRange(left=0, right=2))  # 1
print(obj.sumRange(left=2, right=5))  # -1
print(obj.sumRange(left=0, right=5))  # -3
print(obj.sumRange(left=0, right=0))  # -2
print(obj.sumRange(left=5, right=5))  # -1
