def calc():
	print("Введите какое действие вы хотите  сделать. (+, -, *, /)")
	whattodo = input()
	if whattodo != "+" and whattodo != "-" and whattodo != "*" and whattodo != "/": 
		print("Ошибка! Нужно ввести только +, -, * или /")
		print(" ")
		calc()
	else:
		print("Введите два числа с которыми нужно выполнить действие. (После ввода каждого числа нажимайте Enter)")
		x = input()
		y = input()
		if x.isdigit() and y.isdigit():
			x = int(x)
			y = int(y)
			if whattodo == "+":
				result = x + y
				result = str(result)
				print("Результат: " + result)
			elif whattodo == "-":
				result = x - y
				result = str(result)
				print("Результат: " + result)
			elif whattodo == "*":
				result = x * y
				result = str(result)
				print("Результат: " + result)
			else:
				result = x / y
				result = str(result)
				print("Результат: " + result)
		else:
			try:
				x = float(x)
				y = float(y)
				if whattodo == "+":
					result = x + y
					result = str(result)
					print("Результат: " + result)
				elif whattodo == "-":
					result = x - y
					result = str(result)
					print("Результат: " + result)
				elif whattodo == "*":
					result = x * y
					result = str(result)
					print("Результат: " + result)
				else:
					result = x / y
					result = str(result)
					print("Результат: " + result)
			except ValueError:
				print("Введите число!")
	

while True:
	print(" ")
	print(" ")
	calc()