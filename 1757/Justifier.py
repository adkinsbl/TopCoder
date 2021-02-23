# https://community.topcoder.com/stat?c=problem_statement&pm=1757
class Justifier:
	def justify(self, textIn: [str]) -> [str]:
		maxLen = 0
		for l in textIn:
			if len(l) > maxLen:
				maxLen = len(l)
		return [" " * (maxLen - len(x)) + x for x in textIn]
		
j = Justifier()
print(j.justify(["BOB","TOMMY","JIM"]) == ["  BOB",  "TOMMY",  "  JIM"])
print(j.justify(["JOHN","JAKE","ALAN","BLUE"]) == ["JOHN",  "JAKE",  "ALAN",  "BLUE"])
print(j.justify(["LONGEST","A","LONGER","SHORT"]) == ["LONGEST",  "      A",  " LONGER",  "  SHORT"])