# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=13650"

class KitayutaMart2:
	def numBought(self, K: int, T: int) -> int:
		purchased = 0
		while T > 0:
			purchased += 1
			T -= 2**(purchased-1)*K
		return purchased
		
k = KitayutaMart2()
print(k.numBought(100,100) == 1)
print(k.numBought(100,300) == 2)
print(k.numBought(150,1050) == 3)
print(k.numBought(160,163680) == 10)