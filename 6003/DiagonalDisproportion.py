# https://community.topcoder.com/stat?c=problem_statement&pm=6003
class DiagonalDisproportion:
	def getDisproportion(self, matrix: [str]) -> int:
		main = 0
		collateral = 0
		for i in range(0,len(matrix)):
			main += int(matrix[i][i])
			collateral += int(matrix[i][len(matrix)-1-i])
		return main - collateral

d = DiagonalDisproportion()

print(d.getDisproportion(["190","828","373"]) == 1)
print(d.getDisproportion(["9000","0120","0000","9000"]) == -1)
print(d.getDisproportion(["6"]) == 0)
print(d.getDisproportion(["7748297018","8395414567","7006199788","5446757413","2972498628",
"0508396790","9986085827","2386063041","5687189519","7729785238"]) == -24)