sometext = "12+45"
sometextinlist = list(sometext)
for i in range(len(sometextinlist)):
	a = sometextinlist[i]
	b = ""
	c = ""
	d = ""
	if a.isdigit():
		b += a
		print(b)
	else:
		c += a
		print(c)
		if a.isdigit():
			d += a
		else:
			print("Error")
	if c == "+":
		print(b + d)
