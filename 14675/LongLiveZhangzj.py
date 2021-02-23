# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=14675"

class LongLiveZhangzj:
	def donate(self, speech: [str], words: [str]) -> int:
		lives = 0
		for word in speech:
			if word in words:
				lives += 1
		return lives
		
l = LongLiveZhangzj()
print(l.donate(["make", "topcoder", "great", "again"],["make", "america", "great", "again"]) == 3)
print(l.donate(["toads"],["toad"]) == 0)
print(l.donate(["a", "a"],["a"]) == 2)
print(l.donate(["je", "le", "ai", "deja", "vu", "et", "je", "le", "veux", "encore"],["i", "am", "having", "deja", "vu", "please", "stop", "the", "encore"]) == 3)