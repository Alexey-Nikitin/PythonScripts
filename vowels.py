print("Введите стих, отделяя сторки нажатим Enter, последней строкой введите 'Конец'")
while True:
	s = input()
	if(s == "конец" or s == "Конец" or s == "КОНЕЦ"):
		break
	k = 0
	for x in s:
		if(x in "уеыаоэяию"):
			k += 1
	print(k)