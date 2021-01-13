# https://community.topcoder.com/stat?c=problem_statement&pm=7263
class Sortness:
	def getSortness(self, a: [int]) -> float:
		vals = []
		for i in range(len(a)):
			gt = filter(lambda x: x > a[i], a[0:i])
			lt = filter(lambda x: x < a[i], a[i+1:])
			vals.append(len(list(lt)+list(gt)))
		return sum(vals)/len(vals)

s = Sortness()
print(s.getSortness([3,2,1,4,6,7,5,8]) == 1.25)
print(s.getSortness([1,2,3]) == 0.0)
print(s.getSortness([5,4,3,2,1]) == 4.0)
print(s.getSortness([1,5,8,7,9,6,10,12,11,3,4,2]) == 5.166666666666667)