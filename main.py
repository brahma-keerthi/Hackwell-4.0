# import pandas as pd
# import numpy as np

# # Read the csv data file based on headings and convert it to columns
# col_list = ["AreaCode","AreaName","Category","ConditionName","Description","ExtendedSource","localtime","Priority","Source","utcTime","Value","Link1"]
# df = pd.read_csv("data.csv", usecols=col_list)
# arr = df["localtime"].to_numpy()

# print(arr)

import csv
  
# Open file 
with open('data.csv') as file_obj:
      
    # Create reader object by passing the file 
    # object to reader method
    reader_obj = csv.reader(file_obj)
      
    # Iterate over each row in the csv 
    # file using reader object
    # for row in reader_obj:
    #     print(row[1], row[6], row[7])
    print(type(reader_obj))