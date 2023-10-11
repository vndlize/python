import time
usernames = ['hridz','eric','sam','john','admin']
for username in usernames :
    if username == 'admin' :
        print ('Hello admin, would you like to see a status report?')
    else :
        print (f'Hello {username}, thank you for logging in again.')
for i in range (3,0,-1) :
    print (i,end= ' ')
    time.sleep(0.5)
print ('...\nDeleted Username List')

