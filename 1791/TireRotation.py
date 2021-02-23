# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=1791"

class TireRotation:
	def getCycle(self, initial: str, current: str) -> int:
		if initial == current:
			return 1
		rotation = initial
		for i in range(1,4):
			rotation = self.rotate(rotation)
			if rotation == current:
				return i + 1
		return -1
		
	def rotate(self, wheels: str) -> str:
		return wheels[3] + wheels[2] + wheels[0] + wheels[1]
		
		
t = TireRotation()
print(t.getCycle("ABCD","ABCD") == 1)
print(t.getCycle("ABCD","DCAB") == 2)
print(t.getCycle("ABCD","CDBA") == 4)
print(t.getCycle("ABCD","ABDC") == -1)
print(t.getCycle("ZAXN","XNAZ") == 4)