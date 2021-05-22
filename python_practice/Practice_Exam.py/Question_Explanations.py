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



# Jack will get {'i', 'm', 'd', 'o', 'n'} on performing the operation game1 - game2, which gives letters in game1 but not in game2. 
# He will get {'a', 'b', 't'} on performing the operation game1 & game2, which gives letters in both game1 and game2.
game1 = set ('badminton')
game2 = set ('basketball')
print(game1 - game2)
print(game1 & game2)



# The tuple data type will be created by printing the given code. In Python, the only tuple is a data type that can be created simply
#  by putting different comma-separated values. Also, the tuple can be created by enclosing the sequence of items in parentheses. Here' the output of the given code:
details = 'john', 1993, 10, 'Williams'
print(type(details))


# In the above code, the boolean literals True and False are used. In the Python language, True represents the value as 1 and False as 0. 
# The value of x is True because 1 is equal to True and the value of y is False because 1 is not equal to False. Similarly, these are used in
#  numeric expressions as the value. The value of a is 6 because True is added, which has the value of 1 with 5 and b is 20 because False is
#  added having the value of 0 with 20.
x = (1 == True)
y = (1 == False)
a = True + 5
b = False + 20
print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

# Jack will use the print(pow[-1]) code segment to get the desired output as the index -1 will give 10 as the value of the variable x. 
# Therefore, on evaluating the 2 ** 10 expression, it results in 1024 which is the desired output. Here's the complete code to get the desired output:
pow = [2 ** x for x in range(0, 11)]
print(pow[-1])
print(pow)

# Ethan will use the following code is used to line of code will print two asterisks (*) in two separate lines as the range is (1,4,2) and the end argument 
# is not used in the print statement:
for i in range(1, 4, 2):
    print("*")


# The list.index('a', 4) command of the index() method finds the element a after the fourth index is searched.
#  So, the next a after the index 4 is at the index 6.
list = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b']
print(list.index('a', 4))


# the last number includes the step by how much the print statements slice
s = 'Programming'
print(s[3::])
print(s[::-1])
print(s[1:10:2])
print(s[:-1:1])


# In the given output, the __doc__ attribute is used to print the documentation string of a function.
def double(num):
    """Function to double the value"""
    return 2*num
print(double.__doc__)


# The output of the three print statements in the given code will be 10, <function MyClass.f at 0x000001E704D6B488>, and This is my class in the same order
#  as in the code. 
# When the object accesses the attribute n, its value is printed.
# When the object accesses the function f, the hexadecimal position is printed.
# When the object accesses the docstring, the content of the docstring is printed.
class MyClass:
    """This is my class."""
    n = 10
    def f(self):
        print("Hello World!")
print(MyClass.n)
print(MyClass.f)
print(MyClass.__doc__)


# Ethan will use the items() looping method for this purpose as this method is used to loop through dictionaries 
# and at the same time retrieve the key and its corresponding value of the dictionary.


# List comprehension is used to combine the elements of the two lists, namely, n1 and n2 and generates a new one where elements of both the lists are equal.
print([(n1,n2) for n1 in ['a', 'b', 'c'] for n2 in ['c', 'b', 'd'] if n1==n2])


# In the code, for the first line of output, cat is the positional argument and fill, align, and width are the keyword arguments. 
# These keyword arguments are not retrieved as normal strings to be printed but are retrieved as the actual format codes in the template string. 
# The arguments replace the corresponding named placeholders and the string cat is formatted accordingly. For the second line of output, 123.24 is the
# positional argument and align, width, and precision are the keyword arguments, which tells that the width is 6 and precision is at two decimal places as the
# desired output. Here's the complete code:
string = "{:{fill}{align}{width}}"
print(string.format('cat', fill='*', align='^', width=7))
num = "{:{align}{width}.{precision}f}"
print(num.format(123.236, align='<', width=6, precision=2))


# Jonas will use the following code to sort the list of fruits a in an alphabetical order using an anonymous function, i.e., the lambda function:
a = ['apple', 'mango', 'banana', 'cherry', 'kiwi', 'orange']
a.sort(key = lambda a:a[0])
print(a)


# Dev will use student_details(**d) for calling the function student_details() to print the proper details of the student Jack as dictionary d 
# can deliver the keyword arguments with the ** operator. Here's the complete code:
def student_details(ID, name="Nancy", age=14, section="A"):
   print("Name of the student is", name)
   print("Identity number of the student is", ID)
   print("Age of the student is", age)
   print("Section of the student is", section)
d = {'ID': 1, 'name': 'Jack', 'age': 16, 'section': 'B'}
student_details(**d)

