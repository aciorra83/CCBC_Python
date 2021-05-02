summation = lambda first, second : first + second
print(summation(6, 9))



# syntax of map() is as follows
# map(func, iterable) func = function name, iterable = list or other iterables
numbers = [2, 4, 6, 8, 10]
# map iterates over the items in the list and applies the lambda funtion(squared) to each item in the list
squared = list(map(lambda num: num**2, numbers))
print(squared)

answer = lambda number, power: number**power
print(answer(2,4))


