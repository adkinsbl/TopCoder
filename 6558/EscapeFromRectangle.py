# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=6558"

class EscapeFromRectangle:
	def shortest(self, x: int, y:int, w: int, h: int) -> int:
		return min([abs(x),abs(x-w),abs(y),abs(y-h)])
		
e = EscapeFromRectangle()
print(e.shortest(1,1,5,5) == 1)
print(e.shortest(6,2,10,3) == 1)
print(e.shortest(653,375,1000,1000) == 347)
print(e.shortest(161,181,762,375) == 161)