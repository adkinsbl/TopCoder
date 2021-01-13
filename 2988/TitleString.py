# https://community.topcoder.com/stat?c=problem_statement&pm=2988
# typically I would do this with regular expressions

class TitleString:
	def toFirstUpperCase(self,title:str) -> str:
		chars = list(title)
		if len(title) == 0:
			return("")
		if len(title) == 1:
			return(title.upper())
		
		chars[0] = chars[0].upper()
		for i in range(1,len(title)):
			if title[i] != " " and title[i-1] == " ":
				chars[i] = chars[i].upper()
		return("".join(chars))
		
		
t = TitleString()
print(t.toFirstUpperCase("introduction to algorithms"))
print(t.toFirstUpperCase("more than  one   space    between     words"))
print(t.toFirstUpperCase("  lord of the rings   the fellowship of the ring  "))
print(t.toFirstUpperCase("  "))
print(t.toFirstUpperCase("i"))
print(t.toFirstUpperCase("the king and i"))
print(t.toFirstUpperCase(""))
