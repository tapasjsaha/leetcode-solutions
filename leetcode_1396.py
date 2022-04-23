# Design Underground System
class UndergroundSystem(object):
    def __init__(self):
        self.current_customers = {}
        self.completed_rides = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.current_customers[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        startStation, startTime = self.current_customers.pop(id)
        if (startStation, stationName) in self.completed_rides:
            self.completed_rides[(startStation, stationName)].append(t - startTime)
        else:
            self.completed_rides[(startStation, stationName)] = [t - startTime]

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        rideList = self.completed_rides[(startStation, endStation)]
        return float(sum(rideList)) / len(rideList)


# Your UndergroundSystem object will be instantiated and called as such:
obj = UndergroundSystem()
obj.checkIn(45, "Leyton", 3)
obj.checkIn(32, "Paradise", 8)
obj.checkIn(27, "Leyton", 10)
obj.checkOut(45, "Waterloo", 15)
obj.checkOut(27, "Waterloo", 20)
obj.checkOut(32, "Cambridge", 22)
print(obj.getAverageTime("Paradise", "Cambridge"))
print(obj.getAverageTime("Leyton", "Waterloo"))
obj.checkIn(10, "Leyton", 24)
print(obj.getAverageTime("Leyton", "Waterloo"))
obj.checkOut(10, "Waterloo", 38)
print(obj.getAverageTime("Leyton", "Waterloo"))

# Testcase 2
obj = UndergroundSystem()
obj.checkIn(10, "Leyton", 3)
obj.checkOut(10, "Paradise", 8)
print(obj.getAverageTime("Leyton", "Paradise"))
obj.checkIn(5, "Leyton", 10)
obj.checkOut(5, "Paradise", 16)
print(obj.getAverageTime("Leyton", "Paradise"))
obj.checkIn(2, "Leyton", 21)
obj.checkOut(2, "Paradise", 30)
print(obj.getAverageTime("Leyton", "Paradise"))
