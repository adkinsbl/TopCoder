# https://www.topcoder.com/stat?c=problem_statement&pm=15701
class HockeyPlayoff():
	def __init__(self,winsNeeded: int,AwinHome: int,BwinHome: int):
		self.M = 2*winsNeeded-1
		pass
		
	def winProbability(self):
		pass
		
series = HockeyPlayoff(4,0.7,0.6)
print(series.M)