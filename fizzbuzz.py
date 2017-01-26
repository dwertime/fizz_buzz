n = 100
print("fizz buzz counting up to {}".format(n))
for number in range(1,n):
	if number % 3 == 0 and number % 5 == 0:
		print("fizz buzz")
	elif number % 3 == 0:
		print("fizz")
	elif number % 5 == 0:
		print("buzz")
	else:
		print(number)

	