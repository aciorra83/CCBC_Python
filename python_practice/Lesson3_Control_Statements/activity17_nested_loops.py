# Write a simple nested loop example that sums the even and odd numbers between 1 and 11 and prints out the computation.

# set the loop for even number range
for even in range(2, 11, 2):
# set the loop for odd number range
    for odd in range(1, 11, 2):
        value = even + odd
        print(even, "+", odd, "=", value)