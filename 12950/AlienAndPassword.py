# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=12950"

class AlienAndPassword:
	def getNumber(self, S: str) -> int:
		passwords = set()
		
		for i in range(len(S)):
			passwords.add(S[:i] + S[i+1:])
		
		return len(passwords)
		
a = AlienAndPassword()
print(a.getNumber("A") == 1)
print(a.getNumber("ABA") == 3)
print(a.getNumber("AABACCCCABAA") == 7)
print(a.getNumber("AGAAGAHHHHFTQLLAPUURQQRRRUFJJSBSZVJZZZ") == 26)
print(a.getNumber("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ") == 1)