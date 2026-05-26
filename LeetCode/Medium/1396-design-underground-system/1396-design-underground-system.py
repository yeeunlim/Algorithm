class UndergroundSystem:

    def __init__(self):
        # check_in_map: { id: (start_station, check_in_time) }
        self.check_in_map = {}
        
        # route_map: { (start_station, end_station): [total_time, count] }
        self.route_map = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_map[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, check_in_time = self.check_in_map.pop(id)
        travel_time = t - check_in_time
        route = (start_station, stationName)
        
        self.route_map[route][0] += travel_time
        self.route_map[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        total_time, count = self.route_map[route]

        avg_time = total_time / count
        return avg_time


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)