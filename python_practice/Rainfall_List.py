months = [0] * 12

for i in range(12):
    months[i] = int(input('Enter monthly rainfall: '))

print(months)
sum = 0
min = months[0]
max = months[0]
for i in range(12):
    sum = sum + months[i]
    if months[i] < min:
        min = months[i]
    if months[i] > max:
        max = months[i]

print('yearly rainfall', sum)
print('monthly average', sum/12)
print('Minimum rainfall', min)
print('Maximum rainfall', max)
