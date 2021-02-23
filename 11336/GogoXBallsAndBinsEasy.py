# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=11336"

class GogoXBallsAndBinsEasy:
	def solve(self, T: [int]) -> int:
		moves = 0
		while len(T) > 1:
			moves += T[-1] - T[0]
			T = T[1:-1]
		return moves
		
		
g = GogoXBallsAndBinsEasy()
print(g.solve([0,2,5]) == 5)
print(g.solve([5,6,7,8]) == 4)
print(g.solve([0, 1, 2, 10]) == 11)
print(g.solve([1, 2, 3, 4, 5, 6, 7, 8]) == 16)