age_user = input('Enter your age: ')
age = int(age_user)
if age<2:
	print ('The person is a baby.')
elif age<4:
	print ('The person is a toddler.')
elif age<13:
	print ('The person is a kid.')
elif age<20:
	print ('The person is a teenager.')
elif age<65:
	print ('The person is an adult.')
else:
	print ('The person is a elder.')