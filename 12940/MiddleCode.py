# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=12940"

class MiddleCode:
	def encode(self, s: str) -> str:
		t = ''
		while len(s) > 0:
			if len(s) % 2 == 0:
				mid = len(s) // 2
				l = min(s[mid-1:mid+1])
				idx = mid - 1 + s[mid-1:mid+1].find(l)
				t += l
				s = s[:idx] + s[idx+1:]
			else:
				mid = len(s) // 2
				t += s[mid]
				s = s[:mid] + s[mid + 1:]
		return t
		
m = MiddleCode()
print(m.encode("word") == "ordw")
print(m.encode("aaaaa") == "aaaaa")
print(m.encode("abacaba") == "caabbaa")
print(m.encode("shjegr") == "ejghrs")
print(m.encode("adafaaaadafawafwfasdaa") == "afawadafawafaafsadadaa")