# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=10505"
class SoccerLeagues:
	def points(self, matches):
		scores = [0 for i in range(len(matches))]
		
		for i, results in enumerate(matches):
			for j, result in enumerate(results):
				if i != j:
					if result == 'W':
						scores[i] += 3
					elif result == 'D':
						scores[i] += 1
						scores[j] += 1
					elif result == 'L':
						scores[j] += 3
		return scores
		
		
s = SoccerLeagues()
print(s.points(["-WW","W-W","WW-"]) == [6, 6, 6])
print(s.points(["-DD","L-L","WD-"]) == [5, 2, 8])
print(s.points(["-DWWD",
 "L-WLL",
 "DD-WD",
 "DDL-L",
 "DDLL-"]) == [14, 7, 12, 8, 10])
print(s.points(["-LWWLWDLDWWWWWWDDWDW",
 "D-WWLDDWDWDLWDDWLWDD",
 "LL-DLDWDLDLDWWWLWDDW",
 "LDD-LLLDLWLWWWWDWDWL",
 "LWWW-DWDLWDWDWWWDWDW",
 "DLLWD-WWLLDDDLWWDWWW",
 "WWLWDL-LLDWWWWWDWWLW",
 "LLLLLDW-LDLWDDLLLDWL",
 "DWWWWDDD-DWWWWDWWWDW",
 "WWWWLLLWL-LWWWWWLWWW",
 "DWWWWWWWLW-WDWWWWWWW",
 "DDDLLLDWWWL-DDWDWLDD",
 "LWLWLDLLLDLW-DDDWWDD",
 "LLWWLWDDLWLWL-WWWDLL",
 "WWWWLLDDDWLWDD-WWWLW",
 "DLDLLLWWLLLWWLW-DWLL",
 "DLWWWLDLWWDWWDWL-WWD",
 "LLDDLLWLLWLWLDLWW-WW",
 "LLWLLLWWLWLWWDWWLD-W",
 "LLWDLWDWDWLLWWDDWWL-"]) == [72, 62, 41, 41, 83, 63, 53, 35, 86, 50, 90, 32, 34, 41, 45, 36, 51, 32, 51, 45 ])