# https://community.topcoder.com/stat?c=problem_statement&pm=13159
class FibonacciDiv2:
	def find(self, N: int) -> int:
		seq = [0,1]
		while seq[-1] < N:
			seq.append(seq[-1] + seq[-2])
		print(seq)
		return min(abs(seq[-2] - N), abs(seq[-1] - N))
		
f = FibonacciDiv2()
print(f.find(1) == 0)
print(f.find(15) == 2)
print(f.find(13) == 0)
print(f.find(19) == 2)
print(f.find(1000000) == 167960)
		
		