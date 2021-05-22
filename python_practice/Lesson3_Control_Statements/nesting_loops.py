groups = [[1, 2, 3], [4,5,6,], [7, 8, 9]]
# Loop through the list of number groups
for group in groups:
# loop over the numbers in the group within groups
    for num in group:
        square = num ** 2
        print(num, "squared is ", square)
