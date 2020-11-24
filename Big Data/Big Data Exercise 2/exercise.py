import numpy as np
import pandas as pd
import os

#INTECH IT EXERCISE
#Author: Chanon Kachorn


#loading the data
data = pd.read_csv(os.getcwd() + "\Desktop\IT course October 2020\Big Data Exercise 2\SampleData2.csv", delimiter=',')

# print(data) #TEST that the reading is actually working and we've read the correct file


#BASIC LEVEL QUESTIONS
####################################################################################################
# How many columns are there in the file? Give the number and the name of each column
# print (data.columns) #7 employee_id', 'employee_firstname', 'employee_lastname', 'salary',
                     #'gender', 'department', 'office'
# print(data.info)


# How many employees are there in total?
# print(len(data)) # 23 thousand
# print(data)


# How many departments and offices are there? Give numbers and the name of the department/office
# print(data.department.unique()) #5 ['Engineering' 'Marketing' 'Human-Resource' 'IT' 'Finance']
# print(data.office.unique()) #3 ['Sydney' 'Brisbane' 'Melbourne']


# What is the average salary?
# print(data['salary'].mean()) #54634.5868


# How many employees are male and female?
# print(data[data.gender == 'Male'].count()) #11451 male
# print(data[data.gender == 'Female'].count()) #11549 female

# Who has the employee ID of 05-1101655, give his/her name
# print(data[data.employee_id == '05-1101655']) #Edgardo Anthonies

# What is the employee ID of the person named Federico Kibble?
# print(data[(data.employee_firstname == 'Federico') & (data.employee_lastname == 'Kibble')]) #19-4107144


#INTERMEDIATE LEVEL QUESTIONS
#######################################################################################################


# Which office has the most/least number of employees?
# print(data.groupby('office').count()) #Brisbane 7641, Melbourne 7654, Sydney 7705
                                            #So Sydney is highest and Brisbane is lowest
# print(data.groupby('office').count().sort_values('employee_id')) <- could also do this



# What is the average salary of male and female?
# print(data.groupby('gender').mean()['salary']) #female 54955.529, male 54310.897

# Which office has the highest/lowest average salary? (not by gender, but overall)
# print(data.groupby('office').mean()['salary']) # Brisbane 54860.4373, Melbourne 54638.1390, Sydney 54407.083
                                               # Brisbane is highest and Sydney is lowest


# Which office has the most/least male/female employee?
# print(data.groupby(['office','gender']).count()['employee_id']) # Brisbane male: 3781, female: 3860. Melbourne: male 3864, femle: 3790
                                                 # Sydney male: 3806, female: 3899. Most male at Melbourne, least at Brisbane
                                                 # Most female at Sydney, least at Melbourne


# How many employees have the first_name Ben?
# print(data[data.employee_firstname == 'Ben']) #2 Ben McGeown, Ben Witnall


# How many employees are there in each department?
# print(data.groupby('department').count()) #Engineering 4525, Finance 4671, Human-Resource 4582, IT 4661, Marketing 4561


# Which department has the highest/lowest average salary?
# print(data.groupby('department').mean()['salary']) #Engineering       55059.390276, Finance           53938.648255
                                                    #Human-Resource    54770.753383, IT                55139.886505
                                                    #Marketing         54272.687349. Finance is lowest, IT is highest

#ADVANCED LEVEL QUESTIONS
######################################################################################################

# For each office, which department has the highest/lowest average salary?
# print(data.groupby(['office', 'department']).mean())
# print(data.groupby(['office', 'department']).mean().sort_values('salary'))

# Brisbane  Engineering     55611.801993 <-- highest
#           Finance         54270.134896
#           Human-Resource  54265.287599 <-- lowest
#           IT              54758.798710
#           Marketing       55437.949698

# Melbourne Engineering     55047.007402
#           Finance         53842.963924
#           Human-Resource  55050.633709
#           IT              55582.313269 <-- highest
#           Marketing       53706.120443 <-- lowest

# Sydney    Engineering     54529.417210
#           Finance         53692.460317 <-- lowest
#           Human-Resource  54991.732521
#           IT              55080.586845 <-- highest
#           Marketing       53707.394394

# For each office, which department has the highest/lowest number of male/female?
# print(data.groupby(['office', 'department', 'gender']).count())
# Brisbane  Engineering    Female          770
#                          Male            735
#           Finance        Female          788 
#                          Male            791      <-- highest male
#           Human-Resource Female          775 
#                          Male            741      <-- lowest male
#           IT             Female          793      <-- highest female
#                          Male            757             
#           Marketing      Female          734       <-- lowest female      
#                          Male            757             

# Melbourne Engineering    Female          778       <-- highest female    
#                          Male            708         <-- lowest male 
#           Finance        Female          760                
#                          Male            820        <-- highest male      
#           Human-Resource Female          737      <-- lowest female               
#                          Male            770                 
#           IT             Female          742                
#                          Male            803                 
#           Marketing      Female          773                 
#                          Male            763   
#               
# Sydney    Engineering    Female          768                 
#                          Male            766                 
#           Finance        Female          800                 
#                          Male            712     <-- lowest male          
#           Human-Resource Female          756     <-- lowest female           
#                          Male            803      <-- highest male      
#           IT             Female          768                
#                          Male            798               
#           Marketing      Female          807       <-- highest female        
#                          Male            727            

# Is there anyone in the Melbourne office with the name Diana?
# print(data[(data.office == 'Melbourne') & (data.employee_firstname == 'Diana')])
# 8078   36-3550780              Diana             Kares   92403  Female  Marketing  Melbourne
# 11917  89-0317751              Diana            Patman   72974  Female         IT  Melbourne
# 19152  32-0216308              Diana          Semeniuk   56453  Female         IT  Melbourne
# 21432  97-1099111              Diana       Fassbindler   45374  Female         IT  Melbourne


# How many employees are earning >= 50000??
# print(data[data.salary >= 50000].count() #12656 people


# Sort employee first name alphabetically, who is the first and last person?
# print(data.sort_values('employee_firstname')) #Aaren Churchouse first and Zulema Leighfield last

# Who has the highest and lowest salary? Give their salary and name
# print(data.sort_values('salary')) #lowest 10011 Jim Gemson and highest Ailsun Moubray 99998


# For each office, how many employees are earning >= 70000?
# print(data[data.salary >= 70000].groupby(['office']).count())
# Brisbane          2522              
# Melbourne         2524         
# Sydney            2499               

# For each department, how many employees are earning >= 80000?
print(data[data.salary >= 80000].groupby(['department']).count())
# Engineering             982                 
# Finance                 955               
# Human-Resource         1018                
# IT                     1024          
# Marketing               980