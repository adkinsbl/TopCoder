# https://community.topcoder.com/stat?c=problem_statement&pm=11954
class GreatFairyWar:
	def minHP(self, dps: [int], hp: [int]) -> int:
		damage = 0
		for i in range(0,len(dps)):
			damage += sum(dps[i:]) * hp[i]
		return damage
		
g = GreatFairyWar()
print(g.minHP([1,2],[3,4]) == 17)
print(g.minHP([1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]) == 55)
print(g.minHP([20,12,10,10,23,10],[5,7,7,5,7,7]) == 1767)
print(g.minHP([5,7,7,5,7,7],[20,12,10,10,23,10]) == 1998)
print(g.minHP([30,2,7,4,7,8,21,14,19,12],[2,27,18,19,14,8,25,13,21,30]) == 11029)
print(g.minHP([1],[1]) == 1)