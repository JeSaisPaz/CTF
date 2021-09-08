a = int(input("Convertir en \n (1)Celcius \n (2)Farenheit"))
if a == 1:
	result = 0
	deg = int(input("Temperature en F >"))
	result = (deg-32)*5/9
	print(result)
elif a == 2:
	result = 0
	deg = int(input("Temperature en C >"))
	result = deg*9/5+32
	print(result)
else:
	print("ERR - Message no. 00002")