# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=12524"

class PrimalUnlicensedCreatures:
	def maxWins(self, initialLevel: int, grezPower: [int]) -> int:
		wins = 0
		strength = initialLevel
		for grez in sorted(grezPower):
			if strength > grez:
				strength += grez // 2
				wins += 1
			else:
				break
		return wins
		
p = PrimalUnlicensedCreatures()
print(p.maxWins(31, [10, 20, 30]) == 3)
print(p.maxWins(20, [24, 5, 6, 38]) == 3)
print(p.maxWins(20, [3, 3, 3, 3, 3, 1, 25]) == 6)
print(p.maxWins(4, [3, 13, 6, 4, 9]) == 5)
print(p.maxWins(7, [7, 8, 9, 10]) == 0)