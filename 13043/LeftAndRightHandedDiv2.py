# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=13043"

class LeftAndRightHandedDiv2:
	def count(self, S: str) -> int:
		collisions = 0
		for i in range(1,len(S)):
			if S[i-1] == 'R' and S[i] == 'L':
				collisions += 1
		return collisions
		
l = LeftAndRightHandedDiv2()
print(l.count("L") == 0)
print(l.count("RRR") == 0)
print(l.count("LRLRLR") == 2)
print(l.count("LLLRRR") == 0)
print(l.count("RLRLRL") == 3)