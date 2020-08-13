# https://community.topcoder.com/stat?c=problem_statement&pm=11031
class TheAirTripDivTwo:
	def find(self,flights: [int], fuel: int) -> int:
		trips = 0
		while fuel > 0 and flights:
			fuel -= flights.pop(0)
			if fuel >= 0:
				trips += 1
		return(trips)

a = TheAirTripDivTwo()
print(a.find([1, 2, 3, 4, 5, 6, 7],10))
print(a.find([7, 6, 5, 4, 3, 2, 1],10))
print(a.find([1],1000))
print(a.find([8, 7, 7, 1, 5, 7, 9],21))