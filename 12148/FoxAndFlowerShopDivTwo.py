# https://community.topcoder.com/stat?c=problem_statement&pm=12148

class FoxAndFlowerShopDivTwo:
	def theMaxFlowers(self,flowers: [str], r: int, c: int):
		self.rows = len(flowers)
		self.cols = len(flowers[0])
		self.flowers = flowers
		
		sums = []
		
		sum = 0
		sums.append(self._countFlowers(0,r,0,self.cols))
		sums.append(self._countFlowers(r+1,self.rows,0,self.cols))
		sums.append(self._countFlowers(0,self.rows,0,c))
		sums.append(self._countFlowers(0,self.rows,c+1,self.cols))
		return(max(sums))
	def _countFlowers(self,startRow,stopRow,startCol,stopCol):
		count = 0
		for i in range(startRow,stopRow):
			for j in range(startCol,stopCol):
				if self.flowers[i][j] == 'F':
					count += 1
		return(count)
		
f = FoxAndFlowerShopDivTwo()
print(f.theMaxFlowers(["F.F",".F.",".F."],1,1))
print(f.theMaxFlowers(["F..", "...", "..."],0,0))
print(f.theMaxFlowers([".FF.F.F", "FF...F.", "..FF.FF"],1,2))
print(f.theMaxFlowers(["F", ".", "F", "F", "F", ".", "F", "F"],4,0))
print(f.theMaxFlowers([".FFF..F...", "FFF...FF.F", "..F.F.F.FF", "FF..F.FFF.", "..FFFFF...", "F....FF...", ".FF.FF..FF", "..F.F.FFF.", ".FF..F.F.F", "F.FFF.FF.F"],4,3))