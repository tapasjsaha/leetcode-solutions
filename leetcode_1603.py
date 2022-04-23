# Design Parking System
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.numberOfCar = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.numberOfCar[carType] > 0:
            self.numberOfCar[carType] -= 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

obj = ParkingSystem(1, 1, 0)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))
