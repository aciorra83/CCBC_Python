release_year = "1991"
# setting the correct condition to 'False' (a 'negative condition') to check whether we should break out of the loop
correct = False
# while the answer is not correct, continue to run the program.
while not correct:
    answer = input("When was Python first released? ")
    if answer == release_year:
        print("Congratulations! That is correct.")
# we've gotten the correct answer and need to set the correct condition to true in order to break the loop
        correct = True
    else:
        print("No, that's not it. Try again\n")
print("Bye!")
