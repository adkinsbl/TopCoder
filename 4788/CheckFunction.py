# https://community.topcoder.com/stat?c=problem_statement&pm=4788
class CheckFunction:
	def __init__(self):
		self.lookup = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}
	def newFunction(self,code: str) -> int:
		value = 0
		for x in code:
			value += self.lookup[x]
		return(value)
		
checker = CheckFunction()
print(checker.newFunction('02468'))
print(checker.newFunction("73254370932875002027963295052175"))