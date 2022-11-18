driving = input('Have you driven before？')
if driving != 'yes' and driving != 'no':
	print('Only enter yes/no')
	raise SystemExit

age = input('How old are you?')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('You have passed the test!')
	else:
		print('Weird! How could you have driven?')
elif driving == 'no':
	if age >= 18:
		print('You can go get a driver license already! Why have you not?')
	else:
		print('Good! You can get a license a few more years later')