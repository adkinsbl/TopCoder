# https://community.topcoder.com/stat?c=problem_statement&pm=14742

class GravityPuzzleEasy:
	def solve(self,board: [str]) -> [str]:
		rows = len(board)
		cols = len(board[0])
		
		hashCounts = []
		for i in range(0,cols):
			hashCount = 0
			for j in range(0,rows):
				if board[j][i] == '#': hashCount += 1
			hashCounts.append(hashCount)
		finalBoard = []
		for i in reversed(range(0,rows)):
			level = rows
			finalRow = ""
			for j in range(0,cols):
				if hashCounts[j] >= i+1:
					finalRow += "#"
				else:
					finalRow += "."
			finalBoard.append(finalRow)
		return(finalBoard)
		
g = GravityPuzzleEasy()
print(g.solve(["#",".","."]))
print(g.solve(["##",".#","#."]))
print(g.solve(["..#.#", "#.#..", "...##"]))
print(g.solve(["#####", "#####", "#####", "#####"]))
print(g.solve(["."]))
