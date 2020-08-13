# https://community.topcoder.com/stat?c=problem_statement&pm=1692
class Yahtzee:
	def maxPoints(self,toss: [int]) -> int:
		faceSums = {1:0,2:0,3:0,4:0,5:0,6:0}
		for x in toss:
			faceSums[x] += x
		return(max(faceSums.values()))
		
y = Yahtzee()
print(y.maxPoints([2, 2, 3, 5, 4]))
print(y.maxPoints([6, 4, 1, 1, 3]))
print(y.maxPoints([5, 3, 5, 3, 3]))