# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=2297"

class BettingMoney:
	def moneyMade(self, amounts: [int], centsPerDollar: [int], finalResult) -> int:
		loss = amounts[finalResult] * centsPerDollar[finalResult]
		gain = sum(amounts[:finalResult] + amounts[finalResult+1:]) * 100
		final = gain - loss
		return final
		
b = BettingMoney()
print(b.moneyMade([10,20,30],[20,30,40],1) == 3400)
print(b.moneyMade([200,300,100],[10,10,10],2) == 49000)
print(b.moneyMade([100,100,100,100],[5,5,5,5],0) == 29500)
print(b.moneyMade([5000,5000],[100,2],0) == 0)
print(b.moneyMade([100],[10],0) == -1000)