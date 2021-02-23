# https://community.topcoder.com/stat?c=problem_statement&pm=12112
class LittleElephantAndBooks:
	def getNumber(self, pages: [int], number: int) -> int:
		print(pages)
		pages.sort()
		print(pages)
		print(pages[0:number-1],pages[-2])
		return sum(pages[0:number-1]) + pages[-2]
		
l = LittleElephantAndBooks()
print(l.getNumber([1, 2], 1) == 1)
print(l.getNumber([74, 7, 4, 47, 44], 3) == 58)
print(l.getNumber([3, 1, 9, 7, 2, 8, 6, 4, 5], 7) == 29)
print(l.getNumber([74, 86, 32, 13, 100, 67, 77], 2) == 80)