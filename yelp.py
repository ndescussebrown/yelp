# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 09:59:01 2020

@author: descn0
"""

# -*- coding: utf-8 -*-

"""

Created on Fri Oct 11 2019



@author: nathalie descusse-brown



This file documents the analysis performed as part of the data science bootcamp pre-assessment

analysis with Python 3.7.3 64-bit

"""

# First we want to explore the data and see what the data look like

import os

import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

import statistics

from datetime import datetime

print("Current Working Directory " , os.getcwd())

df_yelpreviews = pd.read_csv('Yelp_reviews_assessment.csv')
#df_exceluniquebusinessid = pd.read_csv('exceluniquebusinessid.csv')

df_yelpreviews.head()

list(df_yelpreviews.columns) 

#Question 10.a. 
#What is the number of unique businesses in this dataset? 
#The unique identifier of each business is recorded under column "Business_ID".

uniquebusinessid=np.unique(df_yelpreviews['Business_ID']) 
uniquecountbusinessid=len(totalbusinessid) 

print('ANSWER TO QUESTION 10.A')
print('The number of unique businesses in this dataset is:',uniquecountbusinessid)

del uniquecountbusinessid


#Question 10.b. 
#What is the name of the business that has the most reviews in this dataset?
# What percentage of all reviews in this dataset are for this most reviewed business? 
#The unique identifier of each business is recorded under column "Business_ID" and 
#the name of each business is recorded under column "Business_Name".
#Note: Businesses that have the same name but have different business IDs are 
#considered different businesses.


totalbusinessid=df_yelpreviews['Business_ID'].value_counts().index.tolist() 
totalcountbusinessid=df_yelpreviews['Business_ID'].value_counts().values.tolist() 
businessnamemostreviewsid= (df_yelpreviews.loc[df_yelpreviews['Business_ID'] == totalbusinessid[0]])

print('ANSWER TO QUESTION 10.B')
print('The business with the most reviews in this dataset is:',businessnamemostreviewsid.iloc[0]['Business_Name'])

del totalbusinessid,totalcountbusinessid,businessnamemostreviewsid

#Question c.
#Based on this dataset, which cities in the state of Nevada have at least one 
#business with an average star rating equal to 5? The city a business is in is 
#recorded under column "City", the state is recorded under column "State" and 
#the average star rating of a business is recorded under column 
#"Avg_Business_Star_Rating". The state of Nevada is recorded as "NV".

nevadebusinesses= (df_yelpreviews.loc[df_yelpreviews['State'] == 'NV'])
totalbusinessidnv=nevadebusinesses['Business_ID'].value_counts().index.tolist() 
uniquebusinessidnv=np.unique(totalbusinessidnv) 
cities = {}

for businessid in uniquebusinessidnv:
    reviewsind = df_yelpreviews.loc[df_yelpreviews['Business_ID'] == businessid]
    reviewsmean = reviewsind['Avg_Business_Star_Rating'].iloc[0]
    city=reviewsind['City'].iloc[0]
    if reviewsmean==5:
        if city in cities:
            cities[city] +=1
        else:
            cities[city] =1

print('ANSWER TO QUESTION 10.C')
print('The cities in the state of Nevada have at least one business with an average star rating equal to 5 are',list(cities.keys()))

#Question 10.d.
#10. d. Find the city with the highest number of reviews in this dataset. 
#What percentage of reviews of businesses in that city are hotel reviews? 
#A hotel review is recorded under column "Business_Category" as "Hotels & Travel".
# The city a business is in is recorded under column "City".


totalcity=df_yelpreviews['City'].value_counts().index.tolist() 
totalcountcity=df_yelpreviews['City'].value_counts().values.tolist() 

print('ANSWER TO QUESTION 10.D')
print('The city with the highest number of reviews in this dataset is:',totalcity[0])

mostreviewscity= df_yelpreviews.loc[df_yelpreviews['City'] == totalcity[0]]
mostreviewcityhotel = mostreviewscity.loc[mostreviewscity['Business_Category'] == 'Hotels & Travel']


print('The percentage of reviews of businesses in that city that are hotel reviews is:',int(len(mostreviewcityhotel)/len(mostreviewscity)*100))

#del 

#Question 10.e.
#On which day of the week (Monday, Tuesday, Wednesday,...) are most reviews posted 
#in this dataset? The date when a review is posted is recorded under column "Review_Date"..
days = {}

for i in range(0,len(df_yelpreviews['Review_Date'])):
    datereview=datetime.strptime(df_yelpreviews['Review_Date'].iloc[i], '%Y-%m-%d')
    dayreview=calendar.day_name[datereview.weekday()]
    if dayreview in days:
        days[dayreview] +=1
    else:
        days[dayreview] =1
    
sorted_days = sorted((value, key) for (key,value) in days.items())

print('ANSWER TO QUESTION 10.E')
print('The day of the week where most reviews are posted in this dataset is:',sorted_days[len(sorted_days)-1][1])
