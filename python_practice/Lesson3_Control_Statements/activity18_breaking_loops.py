for number in range(0, 200):
    if number == 0:
        continue
# Define a condition that checks whether the number is divisible by 3.
    elif number % 3 != 0:
        continue
# Define a condition that checks the data type.
    elif type(number) != int:
        continue
    else:
        pass
    print(number)
