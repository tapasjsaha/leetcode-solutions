# Shuffle an Array
class Solution:
    def __init__(self, nums: [int]):
        self.arr = nums

    def reset(self) -> [int]:
        return self.arr

    def shuffle(self) -> [int]:
        from random import sample
        res = sample(self.arr[:], len(self.arr))
        return res

    #    from random import randrange
    #    temp = self.arr[:]
    #    res = []
    #    for i in range(len(temp)-1, 0, -1):
    #        indx = randrange(0, i, 1)
    #        x = temp.pop(indx)
    #        res.append(x)
    #    res.append(temp[0])
    #    return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

obj = Solution([1, 2, 3, 4])
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)
param_1 = obj.reset()
print(param_1)
param_3 = obj.shuffle()
print(param_3)
param_4 = obj.reset()
print(param_4)
param_5 = obj.shuffle()
print(param_5)
