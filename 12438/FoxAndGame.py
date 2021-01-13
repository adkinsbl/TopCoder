# https://community.topcoder.com/stat?c=problem_statement&pm=12438
class FoxAndGame:
	def countStars(self, result: [str]) -> int:
		starCount = 0
		for e in result:
			starCount += e.count("o")
		return starCount

f = FoxAndGame()
print(f.countStars(["ooo","ooo"]) == 6)
print(f.countStars(["ooo", "oo-", "o--"]) == 6)
print(f.countStars(["ooo", "---", "oo-", "---", "o--"]) == 6)
print(f.countStars(["o--", "o--", "o--", "ooo", "---"]) == 6)
print(f.countStars(["---", "o--", "oo-", "ooo", "ooo", "oo-", "o--", "---"]) == 12)
print(f.countStars(["---", "---", "---", "---", "---", "---"]) == 0)
print(f.countStars(["oo-"]) == 2)