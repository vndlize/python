current_users = ['jim','sam','hridz','john','noah']
current_users_lower = [user.lower() for user in current_users]
new_users = ['hridz','charles','twisha','heena','noah']
for user in new_users :
    if user.lower() in current_users :
        print (f'Username unavailable for {user}, Use a different username')
    else :
        print (f'{user} is available')
