# https://community.topcoder.com/stat?c=problem_statement&pm=11631
class DengklekTryingToSleep:
	def minDucks(self, ducks: [int]) -> int:
		count = 0
		for i in range(min(ducks),max(ducks)):
			if i not in ducks:
				count += 1
		return count
		
d = DengklekTryingToSleep()
print(d.minDucks([5, 3, 2]) == 1)
print(d.minDucks([58]) == 0)
print(d.minDucks([9, 3, 6, 4]) == 3)
print(d.minDucks([7, 4, 77, 47, 74, 44]) == 68)
print(d.minDucks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0)