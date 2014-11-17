# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 14:11:18 2014

@author: LaiQX
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





def read_data():
    """
    Load the dataset from the external .csv and .excel file; Transform the dataset to have
    years as the rows and countries as the columns; show the head of the income dataset; 
    return them as pandas data frame    
    
    """
    
    countries= pd.read_csv('../countries.csv')
    try:
        income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx",index_col=u"gdp pc test")
    except:
        print "excel read module not found "
    income = income.T
    print income.head()
    return countries,income




def income_distribution_plot(income_data,year):
    """
    input a dataframe of income and the year, then draw a histogram to roughly show 
    the distribution of the income of the year, and save the graph as a .png file
    """
    income_year = income_data.loc[year]
    plt.figure(figsize=(10,8))
    income_year.hist(bins=100,alpha=0.3,color='k')
    plt.title('Income Distribution of Year %s' % year)
    plt.xlabel('Income per person')
    plt.ylabel('Frequency')
    plt.savefig('Income distribution of year %s' % year)




def merge_by_year(countries,income,year):
    """
    input a year, this funciton will merge the two dataset by region
    return a dataframe with three columns titled 'Country' 'Region'
    and 'Income'
    
    """
    income_year = income.loc[year]
    income_year_df = pd.DataFrame(income_year)
    income_year_reset = income_year_df.reset_index()
    income_year_reset.columns=['Country','Income']
    comb = pd.merge(countries,income_year_reset,on='Country',how='outer')
    return comb
    
def data_explore(dataset,year):
    """
    input a merged data set. useing the histograms and boxplot
    to explore the distribution of the data. save the graph as .png file
    """
    dataset.hist(by='Region',figsize=(10,8),bins=30,alpha=0.3,color='k')
    plt.savefig('income histogram of year %s by region.png'% (year))
    
    dataset.boxplot(by='Region',figsize=(10,8))
    plt.savefig('income boxplot of year %s by region.png'% (year))
    
    
    
def main():
    countries,income = read_data()
#    year=2000
#    income_distribution_plot(income,year)
#    data_year = merge_by_year(countries,income,year)
    year_begin = 2004
    year_end = 2012
    for year in range(year_begin,year_end+1):
        data_year = merge_by_year(countries,income,year)
        data_explore(data_year,year)
    
if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

