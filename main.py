import csv
import numpy as np
  
# Open file     
with open('data.csv') as file_obj:
      
    # Create reader object by passing the file 
    # object to reader method
    reader_obj = csv.reader(file_obj)

    arr = list(reader_obj)
print(arr)    