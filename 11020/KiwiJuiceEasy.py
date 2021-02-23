# https://community.topcoder.com/stat?c=problem_statement&pm=11020
class KiwiJuiceEasy:
	def thePouring(self, capacities: [int], bottles: [int], fromId: [int], toId: [int]) -> [int]:
		self.capacities = capacities
		self.bottles = bottles
		for i in range(len(fromId)):
			self.pour(fromId[i],toId[i])
		return self.bottles
		
	def pour(self, fromId, toId):
		if self.bottles[fromId] > self.capacities[toId] - self.bottles[toId]:
			self.bottles[fromId] -= self.capacities[toId] - self.bottles[toId]
			self.bottles[toId] = self.capacities[toId]
		else:
			self.bottles[toId] = self.bottles[toId] + self.bottles[fromId]
			self.bottles[fromId] = 0
		
k = KiwiJuiceEasy()
print (k.thePouring([20,20],[5,8],[0],[1]) == [0, 13])
print (k.thePouring([10, 10],[5,8],[0],[1]) == [3, 10])
print (k.thePouring([30, 20, 10],[10, 5, 5],[0, 1, 2],[1, 2, 0]) == [10, 10, 0])
print (k.thePouring([14, 35, 86, 58, 25, 62],[6, 34, 27, 38, 9, 60],[1, 2, 4, 5, 3, 3, 1, 0],[0, 1, 2, 4, 2, 5, 3, 1]) == [0, 14, 65, 35, 25, 35])
print (k.thePouring([700000, 800000, 900000, 1000000],[478478, 478478, 478478, 478478],[2, 3, 2, 0, 1],[0, 1, 1, 3, 2]) == [0, 156956, 900000, 856956])