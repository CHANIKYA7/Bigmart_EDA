# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 22:38:36 2021

@author: Chani
"""
#importing all modules as required
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#reading the dataset through pandas, which is shortly noted as pd
bigmart = pd.read_csv("C:/Users/Chani/Documents/Decodr/sample data/Train.csv")


"""info is calling function which gives the information about the dataset contain,
column_names and data_type and number of columns"""
bigmart.info()

"""descibe is also a calling function which gives number of integer elements as count, mean,
standard deviation, minimum value, 25% ,50%, 75% of data, maximum value and finally 
number of integer rows and columns"""
#which will describe only integer values of data
bigmart.describe()

#which will describe not only integer values and also object type
bigmart.describe(include = "all")

#shape is used for to identify number of rows and columns in a dataset
bigmart.shape

#head function used for showing the top 5 rows of a dataset and indexing starts from 0
     # and if you want to print how amny rows want show would you like to give as attribute of head
bigmart.head()

##tail function used for showing the last 5 rows of a dataset
  #and if you want to print how many rows would you like to give as attribute of tail

bigmart.tail()

#isnull() means it's boolean expression whether True or False
#identifying the number of null values in a dataset and giving sum no.of true in a row

bigmart.isnull().sum()


""" Item_Weight  and Outlet_Size are having the null values """

#columns which gives the column names of a dataset and which is not a callable function
bigmart.columns

#value_counts is a callable function which gives the total number of same items
bigmart.Item_Identifier.value_counts()

#unique is a callable function which gives the all types of objects prensent in a 
#particular column and also gives the datatype of elements
bigmart.Item_Identifier.unique()

#nuniue is also a callable function which gives the number of types of objects prensent in a 
#particular column and also gives the datatype of elements
bigmart.Item_Identifier.nunique()

#In continues data finding the outliers we use the boxplot by using the seaborn or matplotlib.pyplot
sns.boxplot(bigmart.Outlet_Location_Type,bigmart.Item_Outlet_Sales)
sns.boxplot(data = bigmart,color = 'blue')
plt.boxplot(bigmart.Item_Visibility)
bigmart.Item_Visibility.nunique()

#removing the column from the dataset/dataframe using the drop function
bigmart_1 = bigmart.drop("Item_Identifier", axis = 1, inplace = True)
bigmart.shape    

#we want to drop multiple columns use [].
bigmart_2 = bigmart.drop(["Item_Identifier","Outlet_Identifier"], axis = 1, inplace = True)
bigmart.shape

#replace function 
bigmart.Item_Fat_Content.unique()
bigmart.Item_Fat_Content.nunique()
bigmart.Item_Fat_Content.value_counts()
sns.catplot(x = 'Item_Fat_Content', data = bigmart,kind ='count')
sns.countplot(bigmart.Item_Fat_Content)
#In this Item_Fat_Content haviing 2 fat types and which are represent in 5 ways and are replacing.
#replacing low fat with LF and str used for characters not for numbers 
bigmart.Item_Fat_Content = bigmart.Item_Fat_Content.str.replace('low fat',"LF") 

#replacing LF with Low Fat and reg with Regular
bigmart.Item_Fat_Content = bigmart.Item_Fat_Content.str.replace('LF', "Low Fat").replace('reg', "Regular")
bigmart.Item_Fat_Content.value_counts()
sns.countplot(bigmart.Item_Fat_Content)

#Item_Visibility which means visibility of a particular product in a mart / probability of seen a particular produc
bigmart.Item_Visibility.median()
bigmart.Item_Visibility.mean()
#incase having outliers we use the median and want to replace 0 with the median. Saving into the same column
bigmart.Item_Visibility = bigmart.Item_Visibility.replace(0,bigmart.Item_Visibility.median())
bigmart.Item_Visibility.min()

#Item_Type
bigmart.Item_Type.unique()
bigmart.Item_Type.nunique()
bigmart.Item_Type.value_counts()
sns.countplot(bigmart.Item_Type)

#Item_MRP is continuous data so we have to check the data having outliers or not
bigmart.Item_MRP.nunique()
bigmart.Item_MRP.isnull().sum()
bigmart.Item_MRP.mean()
bigmart.Item_MRP.median()
plt.boxplot(bigmart.Item_MRP) #no outliersin MRP

#Outlet_Establishment_Year
bigmart.Outlet_Establishment_Year.unique()
bigmart.Outlet_Establishment_Year.nunique()
bigmart.Outlet_Establishment_Year.value_counts()
sns.countplot(bigmart.Outlet_Establishment_Year)

#Outlet_Size
bigmart.Outlet_Size.value_counts()
bigmart.Outlet_Size.isnull().sum()
#outlet_size having null values and which are deal in two ways 1) removing null values and 2) imputaion
#1) removing null values in a column or row, we use dropna() function which will removes all null values and that to we lost data.so, we would like to go with imputation
#bigmart.dropna()

#2)imputaion which means assigning some values to the null values and there are three types of imputaions and are:
   
    #imputaion by mean--1:
        #continuous data without outliers
bigmart.Item_Weight.mean()
bigmart.Item_Weight.fillna(bigmart.Item_Weight.mean(),inplace = True)
bigmart.Item_Weight.isnull().sum()       
    #imputaion by median --2:
        #continuous data with outliers
bigmart.Item_Weight.meadian()
bigmart.Item_Weight.fillna(bigmart.Item_Weight.median(),inplace = True)
bigmart.Item_Weight.isnull().sum()    
    #imputation by mode---3:
        #for discrete data
bigmart.Outlet_Size.isnull().sum()
bigmart.Outlet_Size.unique()
bigmart.Outlet_Size.nunique()        
bigmart.Outlet_Size.value_counts() #having2410 na values so we are giving others to these na values.
bigmart.Outlet_Size.fillna("others",inplace = True) #imputaion by values
bigmart.Outlet_Size.isnull().sum()

# percentage of a null values
bigmart.isnull().mean()




#Outlet_Location_Type
bigmart.Outlet_Location_Type.value_counts()
bigmart.Outlet_Location_Type.isnull().sum()
sns.countplot(bigmart.Outlet_Location_Type)


#Outlet_Type
bigmart.Outlet_Type.value_counts()
bigmart.Outlet_Type.unique()
bigmart.Outlet_Type.nunique()
sns.countplot(bigmart.Outlet_Type)

#Item_Outlet_Sales and it's a continuous data
bigmart.Item_Outlet_Sales.value_counts()
bigmart.Item_Outlet_Sales.nunique()
bigmart.Item_Outlet_Sales.isnull().sum()
sns.countplot(bigmart.Item_Outlet_Sales)
plt.boxplot(bigmart.Item_Outlet_Sales) 
























