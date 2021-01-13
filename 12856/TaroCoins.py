# https://community.topcoder.com/stat?c=problem_statement&pm=12856
import math
import queue

class TaroCoins:
	def getNumber(self,N):
		largestK = math.ceil(math.log(N,2))
		if largestK == 0: largestK = 1
		usableCoins = []
		for k in range(0,largestK):
			usableCoins.append(2**k)
			usableCoins.append(2**k)
		print(usableCoins)
		
t = TaroCoins()
print(t.getNumber(1))
print(t.getNumber(6))