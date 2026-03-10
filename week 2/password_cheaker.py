user = input('enter user name')
password = int(input('enter your password'))
login_pass = 1289
while password!=login_pass:
    password = int(input('enter your password'))
    if password == login_pass:
      print('login successuly')
    else:
      print('enter password again')