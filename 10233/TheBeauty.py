# # URL:"https://community.topcoder.com/stat?c=problem_statement&pm=10233"

class TheBeauty:
	def find(self, n: int) -> int:
		return len(set(str(n)))
	
b = TheBeauty()
print(b.find(7) == 1)
print(b.find(100) == 2)
print(b.find(123456789) == 9)
print(b.find(100000000) == 2)
print(b.find(932400154) == 7)