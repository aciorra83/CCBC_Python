# Complete the Python code to take two integers as the user input and print their average.
number1=int(input())
number2=int(input())
avg = (number1 + number2)/2
print(avg)


# Write the Python code that displays Hello Everyone five times in a single row.
print("Hello Everyone " * 5)


# Complete the Python code that will calculate the area of a square, which takes the side as the user input.
area = int(input())
print(area * area)

# Complete the Python code to calculate and print the day, hour, minutes, and seconds and take time in seconds as the user input.
time_in_sec = float(input())
day = time_in_sec // (24 * 3600)
time_in_sec = time_in_sec % (24 * 3600)
hour = time_in_sec // 3600
time_in_sec %= 3600
minutes = time_in_sec // 60
time_in_sec %= 60
seconds = time_in_sec
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

# Complete the Python code that takes a number as the user input and prints its multiples from 1 to 10.
number = int(input())
for i in range(1, 11):
  print(number, 'x', i, '=', number*i, "<br />")