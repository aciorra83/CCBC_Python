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
