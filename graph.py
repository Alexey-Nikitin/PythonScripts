from tkinter import *  

window = Tk()  
window.title("Калькулятор")  
window.geometry('236x400')  
number1 = ""
number2 = ""
sign = ""
equally_ = ""
def plus():
	global sign
	global number1
	global number2
	global equally_
	if(sign == "+" or sign == "-" or sign == "/" or sign == "*"):
		if(equally_ == int()):
			sign = "+"
			number1 = equally_
		else:
			if(sign == "+"):
				number1 = int(number1) + int(number2)
			if(sign == "-"):
				number1 = int(number1) - int(number2)
			if(sign == "*"):
				number1 = int(number1) * int(number2)
			if(sign == "/"):
				number1 = int(number1) / int(number2)
			sign = "+"
			number2 = ""
			number1 = int(number1)
	if(sign == ""):
		sign = "+"
def minus(): 
	global sign
	global number1
	global number2
	global equally_
	if(sign == "+" or sign == "-" or sign == "/" or sign == "*"):
		if(equally_ == int()):
			sign = "-"
			number1 = equally_
		else:
			if(sign == "+"):
				number1 = int(number1) + int(number2)
			if(sign == "-"):
				number1 = int(number1) - int(number2)
			if(sign == "*"):
				number1 = int(number1) * int(number2)
			if(sign == "/"):
				number1 = int(number1) / int(number2)
			sign = "-"
			number2 = ""
			number1 = int(number1)
	if(sign == ""):
		sign = "-"
def multiply(): 
	global sign
	global number1
	global number2
	global equally_
	if(sign == "+" or sign == "-" or sign == "/" or sign == "*"):
		if(equally_ == int()):
			sign = "*"
			number1 = equally_
		else:
			if(sign == "+"):
				number1 = int(number1) + int(number2)
			if(sign == "-"):
				number1 = int(number1) - int(number2)
			if(sign == "*"):
				number1 = int(number1) * int(number2)
			if(sign == "/"):
				number1 = int(number1) / int(number2)
			sign = "*"
			number2 = ""
			number1 = int(number1)
	if(sign == ""):
		sign = "*"
def divide(): 
	global sign
	global number1
	global number2
	global equally_
	if(sign == "+" or sign == "-" or sign == "/" or sign == "*"):
		if(equally_ == int()):
			sign = "/"
			number1 = equally_
		else:
			if(sign == "+"):
				number1 = int(number1) + int(number2)
			if(sign == "-"):
				number1 = int(number1) - int(number2)
			if(sign == "*"):
				number1 = int(number1) * int(number2)
			if(sign == "/"):
				number1 = int(number1) / int(number2)
			sign = "/"
			number2 = ""
			number1 = int(number1)
	if(sign == ""):
		sign = "/"  

def one():
	if(sign == "+" or sign == "-" or sign == "*" or sign == "/"):
		global number2
		number2 += "1"
	else:
		global number1
		number1 +="1"

def two():
	if(sign == "+" or sign == "-" or sign == "*" or sign == "/"):
		global number2
		number2 += "2"
	else:
		global number1
		number1 += "2"

def three(): 
	if(sign == "+" or sign == "-" or sign == "*" or sign == "/"):
		global number2
		number2 += "3"
	else:
		global number1
		number1 += "3"

def four(): 
	if(sign == "+" or sign == "-" or sign == "*" or sign == "/"):
		global number2
		number2 += "4"
	else:
		global number1
		number1 += "4"

def five(): 
	if(sign == "+" or sign == "-" or sign == "*" or sign == "/"):
		global number2
		number2 += "5"
	else:
		global number1
		number1 += "5"

def six(): 
	if(sign == "+" or sign == "-" or sign == "*" or sign == "/"):
		global number2
		number2 += "6"
	else:
		global number1
		number1 += "6"

def seven(): 
	if(sign == "+" or sign == "-" or sign == "*" or sign == "/"):
		global number2
		number2 += "7"
	else:
		global number1
		number1 += "7"

def eight():
	if(sign == "+" or sign == "-" or sign == "*" or sign == "/"):
		global number2
		number2 += "8" 
	else:
		global number1
		number1 += "8"

def nine(): 
	if(sign == "+" or sign == "-" or sign == "*" or sign == "/"):
		global number2
		number2 += "9"
	else:
		global number1
		number1 += "9"

def zero():
	if(sign == "+" or sign == "-" or sign == "*" or sign == "/"):
		global number2
		number2 += "0" 
	else:
		global number1
		number1 += "0"

def equally():
	global lbl
	global equally_
	global sign
	global number1
	global number2
	if(sign == "+"):
		equally_ = int(number1) + int(number2)
	if(sign == "-"):
		equally_ = int(number1) - int(number2)
	if(sign == "*"):
		equally_ = int(number1) * int(number2)
	if(sign == "/"):
		equally_ = int(number1) / int(number2)
	lbl.configure(text = equally_)
	number2 = ""
	number1 = equally_
	sign = ""

def clear():
	global number1
	global sign
	global number2
	lbl.configure(text = " ")
	sign = ""
	number1 = ""
	number2 = ""

lbl = Label(window, text = " ")
lbl.grid(column = 0, row = 0)
  
btn1 = Button(window, text="1", command = one, height = 5, width = 7)  
btn1.grid(column=0, row=1)
btn2 = Button(window, text="2", command = two, height = 5, width = 7)
btn2.grid(column=1, row=1)  
btn3 = Button(window, text="3", command = three, height = 5, width = 7)  
btn3.grid(column=2, row=1)
btn4 = Button(window, text="+", command = plus, height = 5, width = 7)  
btn4.grid(column=3, row=4)  
btn5 = Button(window, text="4", command = four, height = 5, width = 7)  
btn5.grid(column=0, row=2)  
btn6 = Button(window, text="5", command = five, height = 5, width = 7)  
btn6.grid(column=1, row=2)  
btn7 = Button(window, text="6", command = six, height = 5, width = 7)  
btn7.grid(column=2, row=2)  
btn8 = Button(window, text="-", command = minus, height = 5, width = 7)
btn8.grid(column=3, row=3)  
btn9 = Button(window, text="7", command = seven, height = 5, width = 7)
btn9.grid(column=0, row=3)  
btn10 = Button(window, text="8", command = eight, height = 5, width = 7)  
btn10.grid(column=1, row=3)  
btn11 = Button(window, text="9", command = nine, height = 5, width = 7)  
btn11.grid(column=2, row=3)  
btn12 = Button(window, text="*", command = multiply, height = 5, width = 7)  
btn12.grid(column=3, row=1)  
btn13 = Button(window, text="0", command = zero, height = 5, width = 7)  
btn13.grid(column=1, row=4) 
btn14 = Button(window, text="/", command = divide, height = 5, width = 7)  
btn14.grid(column=3, row=2)  
btn15 = Button(window, text="=", command = equally, height = 5, width = 7)  
btn15.grid(column=2, row=4)
btn16 = Button(window, text="C", command = clear, height = 5, width = 7)  
btn16.grid(column=0, row=4)  
window.mainloop()