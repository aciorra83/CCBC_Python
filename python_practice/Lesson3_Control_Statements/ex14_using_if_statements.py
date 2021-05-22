release_year = "1991"

# setting boolean values for if, elif statements
answer = input("Return True or False: Python was released in 1991. ")
if answer == "True":
    print("Congratulations! That is correct!")
# elif is a combo of 'else' and 'if', allows for a broader comparison scope by chaining multiple if statements
elif answer == "False":
    print("No, that's wrong")
elif answer != ("True" or "False"):
    print("Please anser True or False")

print("Bye Felica!")


# using elif:
answer = input("When was python release: ")
if answer == release_year:
    print("Congratulations! That is correct!")
elif answer > release_year:
    print("That is too late!!")
elif answer < release_year:
    print("That is too early!!")
print("Byeeeee")

