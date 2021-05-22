# The output of the given code will be three stars as the value of the variable i is assigned as 10. The first condition is the while condition in 
# which i should be greater than 0, which is true. So, the while statement prints one star (*) and decrements the value of i by 3 using the 
# assignment operator (-=). The second condition is the if condition in which if i is less than or equal to 3, then the loop breaks. 
# The third condition is the else condition, which prints a star (*) if the above while condition is false. Therefore, the star (*) gets printed 
# three times as on decrementing 10 by 3, the value of the variable i will be 7 firstly and then again on decrementing the value, it will be 4 which 
# is not less than or equal to 3. If the value of the variable i is decremented again, then the if condition becomes true and breaks the loop.

i = 10
while i > 0:  
    i -=3  
    print("*")
    if i <= 3:
         break
else:
    print("*")


# The strip() method will be used to remove the whitespaces from the string s as it returns a copy of the string with both leading and trailing characters stripped.
#  Here's the code to remove extra spaces from the given line of code:
s = ' Python is an object-oriented programming language '
x= s.strip(" ")
print(x)


# The lambda expression is used to print the function a(s). Here, the value of a is 1+2=3 and the print method returns this value.
s = 5
a = lambda s: 1 + 2
print(a(s))

# The following statements are true about inheritance in the Python language:
# Inheritance means passing attributes and methods from a superclass to a subclass.
# Multiple inheritance means that a class has more than one superclass.

# What is the advantage of using the with keyword to open a file?
# The with keyword is good to use when dealing with file objects. The advantage of using the with keyword to open a file is that
# the file is properly closed after its set finishes even if an exception is raised at some point of execution.


# Dev is a beginner in the Python language. He has learned about the bitwise operator and has decided to check his knowledge. He has the following code:
x = 12
y = 5
# Write the code here
result = (x | y & ~y)
print(result)
# Dev will use the result = (x | y & ~y) line of code because this will generate the output as 12. Firstly, the value of y & ~y will be 0. 
# After this value x | y will be evaluated to get the desired output as 12. 

