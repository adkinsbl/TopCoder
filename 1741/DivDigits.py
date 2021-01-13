# https://community.topcoder.com/stat?c=problem_statement&pm=1741

class DivDigits:
	def howMany(self,number: int) -> int:
		divDigits = 0
		for x in str(number):
			if x != '0' and number % int(x) == 0:
				divDigits += 1
		return(divDigits)
		
d = DivDigits()
print(d.howMany(12345))
print(d.howMany(661232))
print(d.howMany(52527))
print(d.howMany(730000000))