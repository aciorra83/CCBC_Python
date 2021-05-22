# Complete the Python code using the if statement block for the statement The computer was invented in 1822:
#   If the user input is given as TRUE, print Correct.
#   If the user input is given as False, print Wrong.
#   If the user input is given as TRUE or FALSE, print Please answer TRUE or FALSE.

answer = input("The computer was invented in 1822:")
if answer == "TRUE":
    print(" Correct")
elif answer == "FALSE":
    print(" Wrong")
elif answer == "TRUE or FALSE":
    print("Please answer TRUE or FALSE")


# Complete the Python code to create a password authentication feature using the while statement. 
# Take ucertify as the user input that prints Welcome Back when the password matches with ucertify, otherwise print Error.

user_pass = input()
# set a negative condition
valid = False
password = "ucertify"
while not valid:
  if password == user_pass:
    print("Welcome back")
# set the original negative condition to true
    valid = True


# Write the Python code to find even numbers between 2 and 100 and print their sum using the for loop and the range function.
total = 0
# range(start, stop, step)
for num in range(2, 101, 2):
# increment by num=2 to loop through range
  total += num
print(total)

# Complete the Python code that will print the cube of the numbers defined in the groups variable.
groups = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# looping over first list
for group in groups:
# looping over numbers within sub lists
  for num in group:
    cube = num ** 3
    print(num, "cube is", cube)