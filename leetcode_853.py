# Car Fleet
class Solution:
    def carFleet(self, target: int, position: [int], speed: [int]) -> int:
        """ Any car which is behind and reaching after is a separate fleet,
        however any car which is behind but reaching on or before is in the same fleet"""
        cars = [x for x in zip(position, speed)]
        cars.sort(key=lambda x: x[0], reverse=True)
        print(cars)
        fleet_count = 0
        prev = 0  # (target + 1) / min(speed)
        for car in cars:
            t = (target - car[0]) / car[1]
            if t <= prev:
                pass
            else:
                prev = t
                fleet_count += 1
        return fleet_count


s = Solution()
print(s.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
print(s.carFleet(target=10, position=[3], speed=[3]))
print(s.carFleet(target=10, position=[0, 4, 2], speed=[2, 1, 3]))
