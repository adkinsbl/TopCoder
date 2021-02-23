# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=13230"

class SumOfPower:
	def findSum(self, array: [int]) -> int:
		powerSum = 0
		for length in range(1,len(array)+1):
			for i in range(0,len(array) + 1 - length):
				powerSum += sum(array[i:i+length])
		return powerSum
			
		
s = SumOfPower()
print(s.findSum([1,2]) == 6)
print(s.findSum([1,1,1]) == 10)
print(s.findSum([3,14,15,92,65]) == 1323)
print(s.findSum([1,2,3,4,5,6,7,8,9,10]) == 1210)