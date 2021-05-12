# creating a file
f = open('myfile.txt', 'w')

# writing something to the new file we just created
print(f.write('Hello, World\n'))
print(f.write('Hello, world again'))

# closing the file
f.close()

# if we want to add need to re-open (this is an append version)
f = open('myfile.txt', 'a')
f.write('More content')
f.close

# reading a file
f = open('myfile.txt', 'r')
print(f.read())
f.close

# combining reading and writing (when writing it appends to last string in doc)
f = open('myfile.txt', 'r+')
print(f.read())
f.write('Some Content')


# Context manager, helps with cleaner code and easier syntax:
with open('myfile.txt', 'r+') as f:
    content = f.read()
    print(content)