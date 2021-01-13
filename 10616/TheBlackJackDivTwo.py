# https://community.topcoder.com/stat?c=problem_statement&pm=10616
class TheBlackJackDivTwo:
	def __init__(self):
		self.vals = {}
		for i in range(2,10):
			self.vals[str(i)] = i
		for v in "TJQK":
			self.vals[v] = 10
		self.vals['A'] = 11
	def score(self, cards: [str]) -> int:
		score = 0
		for c in cards:
			score += self.vals[c[0]]
		return score
		
bj = TheBlackJackDivTwo()
print(bj.score(["4S", "7D"]) == 11)
print(bj.score(["KS", "TS", "QC"]) == 30)
print(bj.score(["AS", "AD", "AH", "AC"]) == 44)
print(bj.score(["3S", "KC", "AS", "7C", "TC", "9C", "4H", "4S", "2S"]) == 60)