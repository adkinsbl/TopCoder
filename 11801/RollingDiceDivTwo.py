# https://community.topcoder.com/stat?c=problem_statement&pm=11801
def toArr(roll):
	arr = []
	for f in roll:
		arr.append(int(f))
	arr.sort()
	return arr

class RollingDiceDivTwo:
	def minimumFaces(self, rolls: [str]) -> int:
		faces = toArr(rolls.pop())
		for r in rolls:
			r = toArr(r)
			for i in range(len(faces)):
				if faces[i] < r[i]:
					faces[i] = r[i]
		return(sum(faces))

		
r = RollingDiceDivTwo()
print(r.minimumFaces(["137", "364", "115", "724"]) == 14)
print(r.minimumFaces(["1112", "1111", "1211", "1111"]) == 5)
print(r.minimumFaces(["24412", "56316", "66666", "45625"]) == 30)
print(r.minimumFaces(["931", "821", "156", "512", "129", "358", "555"]) == 19)
print(r.minimumFaces(["3", "7", "4", "2", "4"]) == 7)
print(r.minimumFaces(["281868247265686571829977999522", "611464285871136563343229916655", "716739845311113736768779647392", "779122814312329463718383927626",
"571573431548647653632439431183", "547362375338962625957869719518", "539263489892486347713288936885", "417131347396232733384379841536"]) == 176)