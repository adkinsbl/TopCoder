# https://community.topcoder.com/stat?c=problem_statement&pm=13004
class MagicalStringDiv2:
	def minimalMoves(self, s: str) -> int:
		mid = len(s) // 2
		minMoves = s[:mid].count("<")
		minMoves += s[mid:].count(">")
		return minMoves
		
m = MagicalStringDiv2()
print(m.minimalMoves(">><<><") == 2)
print(m.minimalMoves(">>>><<<<") == 0)
print(m.minimalMoves("<<>>") == 4)
print(m.minimalMoves("<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><") == 20)