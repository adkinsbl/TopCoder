# https://community.topcoder.com/stat?c=problem_statement&pm=13505
class GreaterGameDiv2:
	def calc(self, snuke: [int], sothe: [int]) -> int:
		score = 0
		for i in range(0,len(snuke)):
			if snuke[i] > sothe[i]:
				score += 1
		return score	
		
g = GreaterGameDiv2()
print(g.calc([1, 3],[4, 2]) == 1)
print(g.calc([1,3,5,7,9],[2,4,6,8,10]) == 0)
print(g.calc([2],[1]) == 1)
print(g.calc([3,5,9,16,14,20,15,17,13,2],[6,18,1,8,7,10,11,19,12,4]) == 6)