# https://community.topcoder.com/stat?c=problem_statement&pm=14300
class MakingPairs:
	def get(self, card: [int]) -> int:
		num = 0
		for c in card:
			num += c // 2
		return num

m = MakingPairs()
print(m.get([2,2,2]) == 3)
print(m.get([1,1,1]) == 0)
print(m.get([5]) == 2)
print(m.get([43,23,10,39,39,22,22,0,3,4,3,2]) == 102)
print(m.get([0]) == 0)