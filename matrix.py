def matrix(n, m):
	print()
	matrix = []
	for i in range(n):
		matrix.append([])
	for x in range(m):
		for y in range(len(matrix)):
			matrix[y].append("0")
			print(matrix[y][x], end = "  ")
		print()

while True:
	print()
	print("Введите количество столбцов, которое хотите получить. (Введите 'Конец', если хотите закончить)")
	number1 = input()
	if(number1 == "конец" or number1 == "Конец"):
		break
	print()
	print("Введите количество строк, которое хотите получить. (Введите 'Конец', если хотите закончить)")
	number2 = input()
	if(number2 == "конец" or number2 == "Конец"):
		break
	if(number1.isdigit() and number2.isdigit()):
		number1 = int(number1)
		number2 = int(number2)
		matrix(number1, number2)
	else:
		print("Нужно ввести число!")
		continue
