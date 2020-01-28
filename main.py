import request, login

LoginAccess = login.mainLogin()

if LoginAccess:
    print("Run the program")
else:
    print("Access denied etc.")
