import random
def random_number_generator(l):
    """
    Generate a list of random numbers of length l.
    """
    output = []
    for i in range(l):
        output.append(random.randint(0, 1000)) 
    return output
print(random_number_generator(3)) # int passed in random_number_generator is the number of ints in output