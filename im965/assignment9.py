# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 20:35:38 2014

@author: Israel
"""
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

###set CD
#os.chdir('C:\Users\Israel\Documents\GitHub\assignment9\im965')

#load countries data
countries = pd.read_csv('countries.csv',header=0,index_col=0)

#Load income data
income = pd.read_excel('gapminder.xlsx',sheetname='Data',header=0,index_col=0)
income = income.T
income.index.name = 'year'
income.columns.name = 'country'
print income.head()


#program to plot distribution in a particular year
def incDist(year=2000):
    '''Plot a histogram and the kernel density of income for input year'''
    data=income.ix[year].dropna()
    
    plt.figure()
    data.hist(bins=100,color='k',normed=True)
    plt.xlim(data.min(),data.max())
    plt.title('World Income Distribution in '+str(year))
    plt.xlabel('GDP Per Capita, PPP-Adjusted $')
    plt.show()
    plt.close()
    
    plt.figure()
    data.plot(kind='kde', style='k--')
    plt.xlim(data.min(),data.max())
    plt.title('World Income Distribution in '+str(year))
    plt.xlabel('GDP Per Capita, PPP-Adjusted $')
    plt.show()
    plt.close()
    
#program to merge income data and country-region
def merge_by_year(year=2000):
    '''Merge region and income data for input year'''
    data = DataFrame(income.ix[year].dropna())
    merged = pd.merge(data,countries,how='outer',left_index=True, right_index=True)
    merged['country']=merged.index
    merged=merged.rename(columns={2000: 'Income'})
    return merged
    
#Explore the last few years

data = merge_by_year(2000)
for year in np.arange(2001,2013) :
   data = pd.merge(data,merge_by_year(year),how='outer')
groups = data.groupby(data.Region)
summary = groups.describe().T
summary.drop(['mean','count','std'],axis=1,level=1,inplace=True)
regions = list(data['Region'].value_counts().index)


for region in regions:
    summary[region].plot()
    plt.title(region)
    plt.savefig(str(region)+'.png')
    plt.close()
    
plt.figure()
summary = summary.swaplevel(1,0,axis=1)
summary['50%'].plot()
plt.title('Mean Income by Region')
plt.savefig('mean_by_region.png')
plt.close()
    
    



 
        



    
    




    


        
