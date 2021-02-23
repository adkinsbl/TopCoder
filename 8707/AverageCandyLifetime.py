# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=8707"

class AverageCandyLifetime:
	def getAverage(self, eatenCandies: [int]) -> float:
		monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		runningDays = 0
		ages = 0
		count = 0
		for i in range(len(eatenCandies)):
			runningDays += monthDays[i]
			if eatenCandies[i] > 0:
				count += eatenCandies[i]
				ages += eatenCandies[i]*runningDays
				
		return ages/count
		
a = AverageCandyLifetime()
print(a.getAverage([1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 60.5)
print(a.getAverage([0, 1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 59.0)
print(a.getAverage([0, 0, 0, 0, 0, 1, 0, 0, 0, 50, 0, 0]) == 301.5882352941176)
print(a.getAverage([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 252.80769230769232)