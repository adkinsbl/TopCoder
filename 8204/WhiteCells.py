# https://community.topcoder.com/stat?c=problem_statement&pm=8204
class WhiteCells:
	def countOccupied(self, board: [str]) -> int:
		count = 0
		for row in range(0,len(board)):
			for col in range(0,len(board)):
				if row % 2 == 0:
					if col % 2 == 0:
						if board[row][col] == 'F':
							count += 1
				else:
					if col % 2 == 1:
						if board[row][col] == 'F':
							count += 1
		return count
		
w = WhiteCells()
print(w.countOccupied(["........","........", "........", "........", "........", "........", "........", "........"]) == 0)
print(w.countOccupied(["FFFFFFFF", "FFFFFFFF", "FFFFFFFF", "FFFFFFFF", "FFFFFFFF", "FFFFFFFF", "FFFFFFFF", "FFFFFFFF"]) == 32)
print(w.countOccupied([".F.F...F", "F...F.F.", "...F.F.F", "F.F...F.", ".F...F..", "F...F.F.", ".F.F.F.F", "..FF..F."]) == 1)
print(w.countOccupied(["........", "..F.....", ".....F..", ".....F..", "........", "........", ".......F", ".F......"]) == 2)