# https://community.topcoder.com/stat?c=problem_statement&pm=13880
class Hexspeak():
	def decode(self,ciphertext: int) -> str:
		hexCipher = hex(ciphertext)
		hexCipher = hexCipher[2:].upper().replace('0','O').replace('1','I')
		numDigits = sum(c.isdigit() for c in hexCipher)
		if numDigits > 0:
			return("Error!")
		else:
			return(hexCipher)
		
h = Hexspeak()
print(h.decode(257))
print(h.decode(258))
print(h.decode(3405691582))
print(h.decode(2882400001))
print(h.decode(999994830345994239))
print(h.decode(1000000000000000000))