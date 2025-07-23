username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "admin123":
        print("You're admin")
    else:
        print("Wrong")
elif username == "user":
    if password == "user123":
        print("You're user")
    else:
        print("Wrong")
else:
    print("Not found")