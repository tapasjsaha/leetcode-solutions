# Closest Dessert Cost
class Solution:
    #    def __init__(self):
    #        self.closeCost = []
    #        self.closeBy = float('inf')

    def closestCost(self, baseCosts: [int], toppingCosts: [int], target: int) -> int:
        self.closeCost = [float('inf')]
        self.closeBy = float('inf')

        def backtrack(current, available):
            if not available:
                if abs(target - sum(current)) < self.closeBy:
                    self.closeBy = abs(target - sum(current))
                    self.closeCost = current
                elif abs(target - sum(current)) == self.closeBy:
                    if sum(current) < sum(self.closeCost):
                        self.closeBy = abs(target - sum(current))
                        self.closeCost = current
            else:
                toping = available.pop(0)
                candidate_list = [toping * i for i in range(3)]
                for candidate in candidate_list:
                    backtrack(current + [candidate], available[:])
                    if self.closeBy == 0:
                        return

        for base in baseCosts:
            backtrack([base], toppingCosts[:])
            if self.closeBy == 0:
                break

        # print(self.closeCost)
        return sum(self.closeCost)


s = Solution()
print(s.closestCost(baseCosts=[1, 7], toppingCosts=[3, 4], target=10))

print(s.closestCost(baseCosts=[2, 3], toppingCosts=[4, 5, 100], target=18))

print(s.closestCost(baseCosts=[3, 10], toppingCosts=[2, 5], target=9))

print(s.closestCost(baseCosts=[10], toppingCosts=[1], target=1))

print(s.closestCost(baseCosts=[716, 4707], toppingCosts=[399, 7161, 1043, 8560, 527, 8067, 117, 1176, 334, 400],
                    target=7371))

print(s.closestCost(baseCosts=[1], toppingCosts=[8, 10], target=10))
