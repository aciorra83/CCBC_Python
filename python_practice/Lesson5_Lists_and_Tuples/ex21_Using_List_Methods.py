#use append method to add elephant to list
wild = ['Lion', 'Zebra', 'Panther', 'Antelope']
wild.append('Elephant')
print(wild)

#extend an empty animals list to wild list
wild = ['Lion', 'Zebra', 'Panther', 'Antelope']
animals = []
animals.extend(wild)
print(wild)

#insert cheetah into wild list at index 2 and replace index 1 with giraffe using insert and pop
wild = ['Lion', 'Zebra', 'Panther', 'Antelope']
wild.insert(2,'Cheetah')
wild.pop(1)
wild.insert(1, 'Giraffe')
print(wild)

#sort elements in wild list
wild = ['Lion', 'Zebra', 'Panther', 'Antelope']
wild.sort(key=None, reverse=False)
print(wild)