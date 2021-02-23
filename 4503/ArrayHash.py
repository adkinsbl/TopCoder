# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=4503"

class ArrayHash:
	def __init__(self):
		self.alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	
	def getHash(self, input: [str]) -> int:
		hashVal = 0
		for element, row in enumerate(input):
			for position, letter in enumerate(row):
				hashVal += self.alphabet.index(letter) + element + position
		return hashVal
		
a = ArrayHash()
print(a.getHash(["CBA", "DDD"]) == 21)

print(a.getHash(["Z"]) == 25)

print(a.getHash(["A",
 "B",
 "C",
 "D",
 "E",
 "F"]) == 30)

print(a.getHash(["ABCDEFGHIJKLMNOPQRSTUVWXYZ",
 "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
 "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
 "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
 "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
 "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]) == 4290)
 
print(a.getHash(["ZZZZZZZZZZ"]) == 295)