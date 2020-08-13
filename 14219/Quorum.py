# https://community.topcoder.com/stat?c=problem_statement&pm=14219
class Quorum:
	def count(self,arr: [int], k: int) -> int:
		return(sum(sorted(arr)[:k]))
		
q = Quorum()
print(q.count([5,2,3],1))
print(q.count([1,1,1,1,1],5))
print(q.count([50,2,9,49,38],3))
print(q.count([20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1],14))