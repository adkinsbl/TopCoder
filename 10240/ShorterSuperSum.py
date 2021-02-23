# https://community.topcoder.com/stat?c=problem_statement&pm=10240
class ShorterSuperSum:
	def calculate(self, k: int, n: int) -> int:
		if k == 0:
			return n
		if k > 0:
			sum = 0
			for i in range(1,n+1):
				sum += self.calculate(k-1,i)
			return sum
		
		
s = ShorterSuperSum()
print(s.calculate(1,3) == 6)
print(s.calculate(2,3) == 10)
print(s.calculate(4,10) == 2002)
print(s.calculate(10,10) == 167960)