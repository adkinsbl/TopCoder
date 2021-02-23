# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=13048"

class MicroStrings:
	def makeMicroString(self, A: int, D: int) -> str:
		microString = str(A)
		res = A-D
		while res >= 0:
			microString += str(res)
			res -= D
		return microString
		
m = MicroStrings()
print(m.makeMicroString(12, 5) == "1272")
print(m.makeMicroString(3, 2) == "31")
print(m.makeMicroString(31, 40) == "31")
print(m.makeMicroString(30, 6) == "3024181260")