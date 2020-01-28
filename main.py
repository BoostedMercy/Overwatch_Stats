import request, login

print("---Main program---")

LoginAccess = login.mainLogin()

if LoginAccess:
    Stats = (request.getAll("pc", "eu", "PocketMercy-2405"))
    print(Stats["name"])
else:
    print("Access denied etc.")
