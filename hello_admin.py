usernames = ['']
for username in usernames:
	if username == 'admin':
		print (f"Hello {username.title()}, Would you like to see today's status report?")
	elif len(username) == 0:
		print ('We need to find some users!')
	else:
		print (f"Hello {username.title()}! Thank you logging in again.")