user_password = "random"
valid = False
while not valid:
    password = input("What is your password?")
    if password == user_password:
        print("Welcome back user!")
        valid = True
    else:
        print("Invalid Password, Try again...")
