# https://community.topcoder.com/stat?c=problem_statement&pm=1667

class CCipher:
	def decode(self,cipherText: str, shift: int) -> str:
		lookup = {}
		stepper = 0
		for i in range(ord('A'),ord('Z')+1):
			if i+shift > ord('Z'):
				lookup[chr(ord('A')+stepper)] = chr(i)
				stepper += 1
			else:
				lookup[chr(i+shift)] = chr(i)
		decodedString = ""
		for x in cipherText:
			decodedString += lookup[x]
		return(decodedString)
		
c = CCipher()
print(c.decode("VQREQFGT",2))
print(c.decode("ABCDEFGHIJKLMNOPQRSTUVWXYZ",10))
print(c.decode("TOPCODER",0))
print(c.decode("ZWBGLZ",25))
print(c.decode("DBNPCBQ",1))
print(c.decode("LIPPSASVPH",4))