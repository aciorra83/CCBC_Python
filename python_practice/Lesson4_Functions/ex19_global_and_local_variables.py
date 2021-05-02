#initializing the global number variable
number = 5
def summation (first, second):
    #adds parameters and global number together
    total = first + second + number
    return total
#call the "summation" function with 2 parameters
outer_total = summation (10, 20)
#Print the initial value of "number"
print("The first number we initialised was " + str(number))
#print the total sum of global variable number and 2 parameters passed into the function
print("The total summation was " + str(outer_total))