# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=13521"

class NamingConvention:
	def toCamelCase(self, variableName: str) -> str:
		words = variableName.split('_')
		camelName = words.pop(0)
		words = [w[0].upper() + w[1:] for w in words]
		camelName += ''.join(words)
		return camelName
		
n = NamingConvention()
print(n.toCamelCase("sum_of_two_numbers") == "sumOfTwoNumbers")
print(n.toCamelCase("variable") == "variable")
print(n.toCamelCase("t_o_p_c_o_d_e_r") == "tOPCODER")
print(n.toCamelCase("the_variable_name_can_be_very_long_like_this") == "theVariableNameCanBeVeryLongLikeThis")