# standard file reading open() function within a context manager with the read mode. 
import csv
# opening with the relative pathfile name
with open('Lesson8_Modules_Packages_File_Operations/Mock_Data.csv', 'r') as f:
    mock_data_reader = csv.reader(f)

    line_count = 1 
    next(mock_data_reader) # skipping line 1 which is the header row 
    for row in mock_data_reader: 
        if line_count > 0: 
            print(row) 
    line_count += 1


# writing to a CSV file
import csv
with open('example.csv','w') as a:
    example_data_writer = csv.writer(a)

    example_data_writer.writerow(['name', 'age'])
    example_data_writer.writerow(['steven', 25])


# Writing a dict to the CSV file:
import csv
with open('people.csv', 'w') as b:
    fields = ['name', 'age']
    people_writer = csv.DictWriter(b, fieldnames = fields)

    people_writer.writeheader() # writes the fields as first row, creates header row
    people_writer.writerow({'name': 'Santa Claus', 'age': 1000}) # written in dict format with key and value pairs