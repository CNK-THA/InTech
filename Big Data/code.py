import numpy as np
import pandas as pd
import os

# use pip install pandas

#loading the data
data = pd.read_csv(os.getcwd() + "\Desktop\IT course October 2020\Big Data\DATA.csv", delimiter=',')

#display first 5 rows
# print(data.head())
#display last 5 rows
# print(data.tail())

#Data filtering
# print(data[data.Gender == 'Female'].head(10))
#data[data.column == 'whatever you want to see'] <--- This is the general syntax for this command!


#Group By
# print(data.groupby('Gender').count())
# print(data.groupby('Department').count())
# print(data.groupby('Shirt Size').count())

#Average
# print(data.groupby('Gender').mean()[['Age']]) #read right to left, average 'age' for each of the 'gender'
# print(data.groupby('Department').mean()[['Salary']])
# print("Average salary is:", data['Salary'].mean()) #average salary (no group by) so for the entire company

#Sorting
# print(data.sort_values('Salary'))
# print(data.sort_values('Salary', ascending=[False]))
# print(data.sort_values('Age').groupby('Department').head())
# print(data.sort_values('Name')) #this one is doing it alphabetically!
print(data.sort_values('Name', ascending=[False]))



















