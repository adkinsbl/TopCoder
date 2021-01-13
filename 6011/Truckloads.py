# https://community.topcoder.com/stat?c=problem_statement&pm=6011
import queue

class Truckloads:
	def numTrucks(self,numCrates: int, loadSize: int) -> int:
		truckLoads = 0
		q = queue.Queue()
		q.put(numCrates)
		while not q.empty():
			crates = q.get()
			if crates > loadSize:
				halfCrates = crates // 2
				if crates % 2 == 0:
					q.put(halfCrates)
					q.put(halfCrates)
				else:
					q.put(halfCrates)
					q.put(halfCrates+1)
			else:
				truckLoads += 1
		return(truckLoads)
		
t = Truckloads()
print(t.numTrucks(14,3))