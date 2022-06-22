import csv

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

    arr = list(reader_obj)

# print(arr) 

print(Sort(arr))

  