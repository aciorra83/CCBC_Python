# Complete the Python code that takes the number of days as the user input
# and converts the days into a number of years and days and then prints them.
days = int(input())

# Calculate the number of years from user input
years = days // 365
# Calculate the remainder of days in a year
days_left = days % 365

print("Years = ", years, " and Days = ", days_left)



# Write the Python code to perform the following string slicing tasks:
#   Print letter s from the given string Cats hate water.
#   Print integer 9 from the given list [8, 9, 10].
#   Print the word math from the given sentence He doesn't teach math.
#   Print 1, 2, 3 from the given statement Testing 1, 2, 3.
#   Print A man, a plan, a canal from the given sentence A man, a plan, a canal: Panama.
print("Cats hate water."[3])
print("[8,9,10]"[3])
print("He doesn't even teach math"[-4:])
print("Testing 1,2,3"[-5:])
print("A man, a plan, a canal: Panama"[0:22])


# Complete the Python code that converts the last n letters of a given string to the uppercase. In this, the string is converted into an integer, 
# specifying the last n letters to convert as the input from a user where n denotes the number of elements.

st = "bougainvillea"
# user input determines how many characters will be in uppercase
n = int(input())
# initialize variable that counts from index 0 of string to the length of the string minus n
start = st[:len(st)-n]
# initialize variable to count from last index of string to length of string minus n to use .upper() method on to uppercase the last letters of the element
end = st[len(st)-n:]
print(start + end.upper())


# Complete the Python code that counts and displays the number of occurrences of a recurrent word, such as, afraid in the given sample input.
# input is:
#       I am not afraid to die. I am not afraid to live. I am not afraid to fail. I am not afraid to succeed.
#       afraid
sentence = input()
query = input()
print(sentence.count("afraid"))


# Complete the Python code that fetches the first n elements from the array where n denotes the number of elements.
array = [55, 12, 37, 831, 57, 16, 93, 44, 22]
n = int(input())
# array[index 0 to user defined index n]
print("Array:", array[0:n])


# Write the Python code to perform the following tasks using Boolean operators:
#   Define an even number 124 and print Even.
#   Define an odd number 123 and then print Odd.

# initialize num variable
num = 20
# create a for loop to see if there is a remainder of num
if num % 2 == 0:
    print("Even")
# else statement for odd
else:
    print("odd")
