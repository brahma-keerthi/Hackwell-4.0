import csv
import numpy as np
import pandas as pd
import os

def sortArea(sub_li):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of 
    # sublist lambda has been used
    sub_li.sort(key = lambda x: x[0])  # Index area = 0
    return sub_li

def sortTime(sub_li):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of 
    # sublist lambda has been used
    sub_li.sort(key = lambda x: x[4]) # Index of time = 4
    return sub_li 

# Reading column wise
df = pd.read_csv("data.csv", usecols = ['AreaCode','AreaName','ConditionName', 'Priority','localtime', 'Source', 'Link1'])

# Converting column read file to csv
df.to_csv("Extra.csv", index=False)

# Open file     
with open('Extra.csv') as file_obj:
      
    # Create reader object by passing the file 
    # object to reader method
    reader_obj = csv.reader(file_obj)

    # Removes the header from the data to be sorted
    arr = list(reader_obj)
    header = arr[0]
    del arr[0]

# Removes the intermediate file Extra.csv
os.remove("Extra.csv")

# Sorts the data based on the data
arr = sortArea(arr)

# Separating the list out based on area code
list = []
j = 0
for i in range(len(arr)-1):
    if arr[i][0] != arr[i+1][0]:
        list.append(arr[j:i+1])
        j = i+1

# print((list[0][0]))

# Sorting based on the time
for i in range(len(list)):
    list[i] = sortTime(list[i])
    # Looking into priority when time is same
    j=0
    while j < (len(list[i])-1):
        if list[i][j][4] == list[i][j+1][4]:
            if int(list[i][j][5]) > int(list[i][j+1][5]):
                list[i].remove(list[i][j+1])
                
            elif int(list[i][j][5]) < int(list[i][j+1][5]):
                list[i].remove(list[i][j])
        j+=1
    
    # Even if priority is equal, look in category and sort
    j = 0
    while j < len(list[i]) - 1:
        if list[i][j][4] == list[i][j+1][4] and list[i][j][5] == list[i][j+1][5]:
            if list[i][j][2] == "Person loitering" and list[i][j+1][2] == "Crowd alert":
                list[i].remove(list[i][j])
            elif list[i][j+1][2] == "Person loitering" and list[i][j][2] == "Crowd alert":
                list[i].remove(list[i][j+1])
        j+=1

# Creating new separate csv file for separate areas
for i in range(len(list)):
    name = str(list[i][0][1])  # Gives name of area
    name += ".csv"     
    with open(name, 'w') as f:
      
        # using csv.writer method from CSV package
        write = csv.writer(f)
      
        write.writerow(header)
        write.writerows(list[i])