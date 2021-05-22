user_password = "random"
# create the negative condition
valid = False
while not valid:
    password = input("What is your password? ")
    if password == user_password:
        print("Welcome back user!")
# valid condition has been met, now set it's value to 'True'
        valid = True
    else:
        print("Invalid Password, Try again...")
