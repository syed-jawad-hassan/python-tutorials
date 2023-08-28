current_users = ['jawad', 'Hammad', 'saud', 'sami', 'ali']
new_users = ['ammaar', 'adeel', 'sami', 'Jawad', 'faizan']
current_lower = [current_user.lower() for current_user in current_users]
for new_user in new_users:
	if new_user.lower() in current_lower:
		print ("This username is already taken. Kindly choose a new one.")
	else:
		print ('This username is available.')
