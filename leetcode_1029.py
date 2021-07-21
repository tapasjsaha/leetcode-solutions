# Two City Scheduling
class Solution:
    def twoCitySchedCost(self, costs):
        num = len(costs) // 2
        a, b = 0, 0
        total = 0
        costs.sort(key=lambda x: (abs(x[0] - x[1]), x), reverse=True)
        for cost in costs:
            if a < num and b < num:
                if cost[0] < cost[1]:
                    a += 1
                    total += cost[0]
                else:
                    b += 1
                    total += cost[1]
            elif a < num:
                a += 1
                total += cost[0]
            else:
                b += 1
                total += cost[1]
        return total


s = Solution()
print(s.twoCitySchedCost(costs=[[10, 20], [30, 200], [400, 50], [30, 20]]))
print(s.twoCitySchedCost(costs=[[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]))
print(s.twoCitySchedCost(costs=[[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]))
