# https://community.topcoder.com/stat?c=problem_statement&pm=1650
class Soccer():
	def maxPoints(self, wins: [int], ties: [int]) -> int:
		points = []
		for i in range(len(wins)):
			points.append(3*wins[i]+ties[i])
		return(max(points))
		
m = Soccer()
print(m.maxPoints([1,4,3,0,0],[3,1,5,3,1]))
print(m.maxPoints([12,45,20,17,48,0],[8,10,53,94,0,100]))
print(m.maxPoints([13,79,26,73,14,89,71,37,89,71,19,59,39],[88,27,5,70,84,94,20,50,2,11,31,22,50]))