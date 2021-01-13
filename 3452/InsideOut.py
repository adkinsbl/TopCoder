# https://community.topcoder.com/stat?c=problem_statement&pm=3452
class InsideOut:
	def unscramble(self, line: str) -> str:
		normal = ""
		mid = len(line) // 2
		front = line[0:mid][::-1]
		back = line[mid:][::-1]
		return front + back
		
i = InsideOut()
print(i.unscramble("I ENIL SIHTHSIREBBIG S") == "THIS LINE IS GIBBERISH")
print(i.unscramble("LEVELKAYAK") == "LEVELKAYAK")
print(i.unscramble("H YPPAHSYADILO") == "HAPPY HOLIDAYS")
print(i.unscramble("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "MLKJIHGFEDCBAZYXWVUTSRQPON")
print(i.unscramble("RUT OWT SNEH HCNERF EERHTEGDIRTRAP A DNA  SEVODELT") == "THREE FRENCH HENS TWO TURTLEDOVES  AND A PARTRIDGE")