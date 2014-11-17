# -*- coding: utf-8 -*-
"""
Created on Monday Nov 17 2014

@author: peter
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Read Country Region Info

countries = pd.read_csv('countries.csv')
countryRegion = countries.set_index('Country') 

# Read Country GDP Info
income = pd.read_excel('gdp.xlsx', index_co = 0)
income = income.T
print income.head()

cleanIncome = income.dropna(axis = 1, how = 'all')


# Function for Question 4

def merge_by_year(incomeDF, regionDF, datayear):
    

    yearIncome = incomeDF.loc[datayear]
    
    yearIncome = yearIncome.dropna()
    
    outDF = pd.concat([regionDF,yearIncome], axis=1, join='inner')
    outDF.columns = ['Region', 'Income']
    
    return outDF
    
# Function for Question 5
# Function to get timeseries of percentiles of income
    
def getDistTS(incomeDF, regionDF, yearRange, region):
    
    percents = [0.75,0.5,0.25]

    out = np.zeros([5,len(yearRange)])
    
    for idx in range(len(yearRange)):
        
        year = yearRange[idx]
        
        mergedDF = merge_by_year(incomeDF, regionDF, year)
        
        # Maxium
        out[0,idx] = mergedDF[mergedDF['Region'] == region]['Income'].max()
        
        # 75%, 50%, 25%
        out[1:4,idx] = np.squeeze(mergedDF[mergedDF['Region'] == region].quantile(percents).values)
        
        # Minimum
        out[4,idx] = mergedDF[mergedDF['Region'] == region]['Income'].min()


        outDF = pd.DataFrame(out, index = ['Max', '75th Percentile', 'Median', '25th Percentile', 'Minimum'], columns = yearRange)
        
    return outDF.T
         

# Question 3

year = 2012

mergedIncomeRegionDF = merge_by_year(cleanIncome, countryRegion, year)
sortedIncomeRegionDF = mergedIncomeRegionDF.sort('Income', ascending = False)

numPanels = 3
dataPerPlot = np.ceil(np.shape(sortedIncomeRegionDF)[0]/numPanels)

fig, axes = plt.subplots(nrows=1, ncols=numPanels)
plt.tight_layout(pad = 4)                

current_palette = sns.color_palette('muted')

regionArray = ['ASIA', 'EUROPE', 'AFRICA', 'NORTH AMERICA', 'SOUTH AMERICA', 'OCEANIA']
colorDict = dict(zip(regionArray,current_palette))

for i in range(numPanels):
    
            startIdx = int((0+(i*dataPerPlot)))
            endIdx = int((dataPerPlot-1)+(i*dataPerPlot))
            
            if i == numPanels - 1:
                tmp = sortedIncomeRegionDF.iloc[startIdx:].copy()
                endIdx = len(sortedIncomeRegionDF)
            else:
                tmp = sortedIncomeRegionDF.iloc[startIdx:endIdx].copy()
            
            
            sortedIncome = tmp.sort('Income', ascending = True)
            sortedIncome['Income'].plot('barh', ax=axes[i], color=sortedIncome.Region.map(colorDict), 
            title = 'rank = ' + str(int(startIdx+1))+' - '+str(int(endIdx+1)))    

plt.suptitle('Inflation Adjusted GDP/Capita , Year = ' + str(year) +'\n (color by region)')

# Question 5
# Plot ts of percentiles by region

regionArray = ['ASIA', 'EUROPE', 'AFRICA', 'NORTH AMERICA', 'SOUTH AMERICA', 'OCEANIA']
yearRange = np.arange(1990,2013)

fig, axes = plt.subplots(nrows = 3, ncols = 2)

for iRow in range(3):
    
    for iCol in range(2):
        
        i = iRow + iCol*3
        
        region = regionArray[i]        
        
        # Get ts by region
        percentileTS = getDistTS(cleanIncome, countryRegion, yearRange, region)
        
        # Plot
        percentileTS.plot(ax=axes[iRow,iCol], title = region)
        plt.suptitle('Distribution of GDP/Capita (Inflation Adjusted) \n 1990 - 2012')
        