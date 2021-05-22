# Complete the Python code for a function named print_arguments that will receive n number of arguments, skip integer values, and print all other value.
def print_arguments(*args):
    for n in args:
        if type(n) == int:
            continue
        print(n)
print_arguments(2, 7.8, "a", 10.0)