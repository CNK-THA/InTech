import numpy as np
import pandas as pd
import os

#INTECH IT EXERCISE
#Author: Chanon Kachorn


#loading the data
data = pd.read_csv(os.getcwd() + "\Desktop\IT course October 2020\Big Data Exercise 3\PowerBI_Data_Exercise_1.csv", delimiter=',')

# print(data) #TEST that the reading is actually working and we've read the correct file





# What is the average age per gender?
# print(data.groupby('gender').mean()['age']) #female 38.742790, male 39.036285

# What is the average salary per age?
# print(data.groupby('age').mean()['salary']) 

# Show average salary per gender Which gender earns more? And what is the average salary for that gender?
# print(data.groupby('gender').mean()['salary']) #Female    54907.213384
#Male      55232.973051

# Show count of shirt size by age
# print(data.groupby('age').count()['shirt_size'])

#Show count of shirt size by gender (hint: split by shirt size)
# print(data.groupby('gender').count()['shirt_size']) #Female    10610
#Male      10390

# Show average age for each location
# print(data.groupby('location').mean()['age']) # Brisbane     38.922693
# Melbourne    38.862789
# Perth        38.761305
# Sydney       39.005924

# Show gender count for each location
# print(data.groupby(['location','gender']).count()['customer'])

# Show average salary for each location
# print(data.groupby('location').mean()['salary'])

# Show marital status count for each age
# print(data.groupby(['marital_status','age']).mean()['customer'])
# At age 27, report numbers of those divorced/married/single
# print(data[data.age == 27].groupby('marital_status').count())

# Show marital status count for each gender
# print(data.groupby(['marital_status','gender']).count()['customer'])
# Are there more single males or females based on percentage?
# c = data.groupby(['marital_status','gender']).count()['customer']
# print(c / c.groupby('marital_status').sum() * 100)


# Show marital status count for each location
# print(data.groupby(['marital_status','location']).count()['customer'])
# Which location has more singles based on percentage? And what is the percentage?
# c = data.groupby(['marital_status','location']).count()['customer']
# print(c / c.groupby('marital_status').sum() * 100)

# Show education count for each gender
# print(data.groupby(['education','gender']).count()['customer'])
# # How many people (in percentage) completed Secondary education for Males and Females?
# c = data.groupby(['education','gender']).count()['customer']
# print(c / c.groupby('education').sum() * 100)

# Show average salary for each education level
# print(data.groupby('education').mean()['salary'])

# Show transport mode for each gender
# print(data.groupby(['transport','gender']).count()['customer'])
# What is the most common transport mode for male/female based on percentage? 
# c = data.groupby(['transport','gender']).count()['customer']
# print(c / c.groupby('transport').sum() * 100)

# # Show transport mode for each location
# print(data.groupby(['transport','location']).count()['customer'])
# # What is the preferred transport mode for each of the location based on percentage?
# c = data.groupby(['transport','location']).count()['customer']
# print(c / c.groupby('transport').sum() * 100)
