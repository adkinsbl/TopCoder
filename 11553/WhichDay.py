# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=11553"

class WhichDay:
	def getDay(self, notOnThisDay: [str]) -> str:
		allDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
		d = [d for d in allDays if d not in notOnThisDay]
		return d[0]
		
w = WhichDay()
print(w.getDay(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]) == "Saturday")
print(w.getDay(["Sunday", "Monday", "Tuesday", "Wednesday", "Friday", "Thursday"]) == "Saturday")
print(w.getDay(["Sunday", "Monday", "Tuesday", "Thursday", "Friday", "Saturday"]) == "Wednesday")
print(w.getDay(["Sunday", "Friday", "Tuesday", "Wednesday", "Monday", "Saturday"]) == "Thursday")