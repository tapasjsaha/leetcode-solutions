# Lemonade Change
class Solution:
    def lemonadeChange(self, bills: [int]) -> bool:
        dchange = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            dchange[bill] += 1
            change = bill - 5
            while change:
                if change >= 10 and dchange[10] != 0:
                    dchange[10] -= 1
                    change -= 10
                else:
                    dchange[5] -= 1
                    change -= 5
            # print(dchange)
            if dchange[5] < 0:
                return False
        return True


s = Solution()
print(s.lemonadeChange(bills=[5, 5, 5, 10, 20]))
print(s.lemonadeChange(bills=[5, 5, 10, 10, 20]))
print(s.lemonadeChange(bills=[5, 5, 10]))
print(s.lemonadeChange(bills=[10, 10]))
