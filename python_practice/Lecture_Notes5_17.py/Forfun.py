# using the relative path allows you to determine the location of where the file is created
t = open("Lecture_Notes5_17.py/Forfun.txt", "a")
t.write("This is fun!")

s = open("Lecture_Notes5_17.py/Forfun.txt", "r")
print(s.read())