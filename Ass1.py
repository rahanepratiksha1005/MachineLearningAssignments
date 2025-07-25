import pandas as pd
# Reading data set
data = pd.read_csv("used_cars_data.csv")
print(data.head(10))
print(data.tail(5))
print(data.info)
# Check duplication
print(data.nunique())
# Missing values calculation
print(data.isnull().sum())
print((data.isnull().sum()/(len(data)))*100)
# Data Reduction - Remove S.No. column from data
data = data.drop(['S.No.'], axis = 1)
print(data.info())
#Features 
#1
from datetime import date
date.today().year
data['Car_Age']=date.today().year-data['Year']
print(data.head())
#2
data['PricePerKM']=data['Price']/data['Kilometers_Driven']
print(data.info())
print(data.head(5))

data['Brand'] = data.Name.str.split().str.get(0)
data['Model'] = data.Name.str.split().str.get(1) + data.Name.str.split().str.get(2)
print(data[['Name','Brand','Model']])


