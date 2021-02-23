# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=6528"

class MedianOfNumbers:
	def findMedian(self, numbers: [int]) -> int:
		if len(numbers) % 2 == 0:
			return -1
		else:
			numbers.sort()
			return numbers[len(numbers) // 2]


m = MedianOfNumbers()
print(m.findMedian([1, 4, 2, 5, 7]) == 4)
print(m.findMedian([1, 5, 8, 3]) == -1)
print(m.findMedian([7]) == 7)
print(m.findMedian([7, 12]) == -1)
print(m.findMedian([66, 53, 47, 86, 18, 21, 97, 92, 15]) == 53)
print(m.findMedian([32, 54, 27, 4, 69, 96, 73, 1, 100, 15, 21]) == 32)