import csv
output = []

# creating csv file with names and hours worked columns
with open('input.csv', 'r') as f:
    mock_data_reader = csv.reader(f)
    output_data = []
    line_count = 1
    for row in mock_data_reader:
        if line_count != 1:
# iterates through the file and multiplies the int(hours worked) by 15
            row[1] = int(row[1]) * 15
            output_data.append(row)
        line_count +=1 

with open('output.csv', 'w') as f:
    fields = ['name', 'wages']
    output_writer = csv.DictWriter(f, fieldnames = fields)

# creates the header row
    output_writer.writeheader()

# input of the dictionary 
    for line in output_data:
        output_writer.writerow(
            {
                'name': line[0], # first index/column
                'wages': line[1] # second index/column
            }
        )

# code won't run beacause there is no input.csv file to read from