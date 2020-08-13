# https://community.topcoder.com/stat?c=problem_statement&pm=12469
class SkiResortsEasy():
	def minCost(self,altitude: [int]) -> int:
		cost = 0
		for i in range(1,len(altitude)):
			if altitude[i] > altitude[i-1]:
				cost += altitude[i] - altitude[i-1]
				altitude[i] = altitude[i-1]
		return(cost)
		
s = SkiResortsEasy()
print(s.minCost([30,20,20,10]))
print(s.minCost([5, 7, 3]))
print(s.minCost([6, 8, 5, 4, 7, 4, 2, 3, 1]))
print(s.minCost([749, 560, 921, 166, 757, 818, 228, 584, 366, 88]))
print(s.minCost([712, 745, 230, 200, 648, 440, 115, 913, 627, 621, 186, 222, 741, 954, 581, 193, 266, 320, 798, 745]))