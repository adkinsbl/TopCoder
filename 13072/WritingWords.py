# https://community.topcoder.com/stat?c=problem_statement&pm=13072
class WritingWords:
	def __init__(self):
		letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.lookup = {}
		for i in range(0,len(letters)):
			self.lookup[letters[i]] = i + 1
	def write(self, word: str) -> int:
		pauses = 0
		for l in word:
			pauses += self.lookup[l.upper()]
		return pauses
	
w = WritingWords()

print(w.write("A") == 1)
print(w.write("ABC") == 6)
print(w.write("VAMOSGIMNASIA") == 143)
print(w.write("TOPCODER") == 96)
print(w.write("SINGLEROUNDMATCH") == 183)
print(w.write("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ") == 1300)