import csv
import numpy as np

def Sort(sub_li):
  
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of 
    # sublist lambda has been used
    sub_li.sort(key = lambda x: x[6])
    return sub_li
  
# Open file     
with open('new.csv') as file_obj:
      
    # Create reader object by passing the file 
    # object to reader method
    reader_obj = csv.reader(file_obj)

    # Removes the header from the data to be sorted
    arr = list(reader_obj)
    header = arr[0]
    del arr[0]
    
arr = Sort(arr)

# Converting sorted list back to the csv file
with open('sorted.csv', 'w') as f:
    write = csv.writer(f)
      
    write.writerow(header) # Writes the header
    write.writerows(arr)  # Writes the rows

  