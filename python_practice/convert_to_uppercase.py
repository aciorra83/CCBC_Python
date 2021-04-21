string = input("Type a string to convert: ")
n = int(input("How many last letters should be converted? "))
# First part of the string
start = string[: len(string) - n]
# last part of string we are converting
end = string[len(string) - n :]
print(start + end.upper())
