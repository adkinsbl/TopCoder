# https://community.topcoder.com/stat?c=problem_statement&pm=16140
import queue

def _gcd(nums: [int]) -> int:
	gcd = 1
	for i in range(1,min(nums)+1):
		res = [x for x in nums if x%i == 0]
		if len(res) == len(nums):
			gcd = i
	return(gcd)

class SquareCityWalking:
	def largestGCD(self,N: int, A: [int]) -> int:
		self.N = N
		self.A = A
		self._getPaths()
		retGCD = -1
		while not self.paths.empty():
			path = self.paths.get()
			vals = self._getPathVals(path)
			thisGCD = _gcd(vals)
			if thisGCD > retGCD:
				retGCD = thisGCD
		return(retGCD)
	def _getPaths(self):
		q = queue.Queue()
		q.put([0])
		validPaths = 1
		while validPaths:
			path = q.get().copy()
			(i,j) = self._idx2cartesian(path[-1])
			newPaths = []
			if i < self.N-1:
				newPaths.append(path + [self._cartesian2idx(i+1,j)])
			if j < self.N-1:
				newPaths.append(path + [self._cartesian2idx(i,j+1)])
			validPaths = 0
			for p in newPaths:
				validPaths += 1
				q.put(p)
		if q.qsize() == 0:
			q.put([0])
		self.paths = q
	def _getPathVals(self,path):
		vals = []
		for x in path:
			vals.append(self.A[x])
		return(vals)
	def _idx2cartesian(self,idx):
		return(idx//self.N,idx%self.N)
	def _cartesian2idx(self,i,j):
		return self.N*i+j

s = SquareCityWalking()
print(s.largestGCD(3,[96, 42, 45,32, 36, 27,40, 54, 84 ]))
print(s.largestGCD(3,[ 4, 9, 2,
  3, 5, 7,
  8, 1, 6  ]))
print(s.largestGCD(4,[54, 81, 27, 36,
  48, 64, 96, 72,
  84, 60, 45, 99,
  80, 90, 40, 63]))
print(s.largestGCD(1,[47]))
print(s.largestGCD(5,[100,  80,  64,  48,  36,
   75,  10,  10,  10,  48,
   50,  10,  10,  10,  64,
   25,  10,  10,  10,  80,
    5,  25,  50,  75, 100]))