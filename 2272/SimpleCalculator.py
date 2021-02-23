# URL:"https://community.topcoder.com/stat?c=problem_statement&pm=2272"

class SimpleCalculator:
	def calculate(self, input: str) -> int:
		for i in range(0, len(input)):
			if input[i] in ['+', '*', '-', '/']:
				num1 = int(input[:i])
				operation = input[i]
				num2 = int(input[i+1:])
				break
		
		if operation == '+':
			return num1 + num2
		elif operation == '-':
			return num1 - num2
		elif operation == '*':
			return num1 * num2
		else:
			return num1 // num2
		
s = SimpleCalculator()
print(s.calculate("5/3") == 1)
print(s.calculate("15*3") == 45)
print(s.calculate("1-10000") == -9999)
print(s.calculate("17+18") == 35)
print(s.calculate("0000000000000018/00000000000000000009") == 2)