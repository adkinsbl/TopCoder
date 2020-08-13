# https://community.topcoder.com/stat?c=problem_statement&pm=10586
class Archery():
	def expectedPoints(self,N: int, ringPoints: [int]) -> float:
		areas = [2*x + 1 for x in range(N+1)]
		totalArea = sum(areas)
		expectedvalue = 0.0
		for i in range(N+1):
			expectedvalue += ringPoints[i]*areas[i]/totalArea
		return(expectedvalue)
		
a = Archery()
print(a.expectedPoints(1,[10,0]))
print(a.expectedPoints(3,[1,1,1,1]))
print(a.expectedPoints(4,[100, 0, 100, 0, 100]))
print(a.expectedPoints(9,[69, 50, 79, 16, 52, 71, 17, 96, 56, 32]))