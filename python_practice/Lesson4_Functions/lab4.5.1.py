# Write the Python code that takes two integer values and returns the first value raised to the power of the second value.
number = int(input())
power = int(input())
squared = lambda number, power: number**power
print(squared(number, power))