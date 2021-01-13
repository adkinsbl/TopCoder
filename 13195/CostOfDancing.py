# https://community.topcoder.com/stat?c=problem_statement&pm=13195
class CostOfDancing:
	def minimum(self, k: int, danceCost: [int]) -> int:
		danceCost.sort()
		return sum(danceCost[0:k])
		
c = CostOfDancing()
print(c.minimum(2,[1,5,3,4]) == 4)
print(c.minimum(3,[1, 5, 4]) == 10)
print(c.minimum(1,[2, 2, 4, 5, 3]) == 2)
print(c.minimum(39,[973, 793, 722, 573, 521, 568, 845, 674, 595, 310, 284, 794, 913, 93, 129, 758, 108, 433, 181, 163, 96, 932,
 703, 989, 884, 420, 615, 991, 364, 657, 421, 336, 801, 142, 908, 321, 709, 752, 346, 656, 413, 629, 801]) == 20431)