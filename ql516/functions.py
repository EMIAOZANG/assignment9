# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 11:46:43 2014

@author: LaiQX
"""

import pandas as pd
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
    print "Q1: The head of the income dataframe"
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
    
def data_explore(dataset,year,mode):
    """
    input a merged data set. useing the histograms or boxplot
    to explore the distribution of the data. save the graph as .png file
    
    mode=='h' : histogram
    mode=='b' : boxplot
    """
    if mode == 'h':
        dataset.hist(by='Region',figsize=(10,8),bins=30,alpha=0.3,color='k')
        plt.savefig('income histogram of year %s by region.png'% (year))
    elif mode == 'b':
        dataset.boxplot(by='Region',figsize=(10,8))
        plt.title(str(year))
        plt.savefig('income boxplot of year %s by region.png'% (year))
    else:
        raise Exception
 

def trend_plot(countries,income,mode,year_start):
    '''
    input the datasets, a start year, and a mode, this function will plot the 
    income trend from the start year to 2012 based on the mode the user choose
    mode=['mean','max','min','median']
    '''
    mode_dict={}
    for year in range(year_start,2012):
        year_data = merge_by_year(countries,income,year)
        region_group = year_data.groupby('Region')
        for name,groups in region_group:
            if mode == 'mean':
                mode_value = region_group.mean().ix[name,'Income']
            elif mode == 'max':
                mode_value = region_group.max().ix[name,'Income']
            elif mode == 'min':
                mode_value = region_group.min().ix[name,'Income']
            elif mode == 'median':
                mode_value = region_group.median().ix[name,'Income']
            else:
                raise Exception
            if (mode_dict.has_key(name)):
                mode_dict[name].append(mode_value)
            else:
                mode_dict[name]=[mode_value]          
    #plot the trend and save it
    color_bar = 'bgrcmyk'   # color used to plot different region
    k=0
    plt.figure(figsize=(10,8))
    for name,groups in region_group:
        colors= color_bar[k]
        k+=1
        plt.plot(range(year_start,2012),mode_dict[name],color=colors,label=name)
    plt.legend(loc=2)
    plt.xlabel('year')
    plt.ylabel('%s Income' % (mode))
    plt.title('Income trend by region using data %s ' % (mode))
    plt.savefig('Income trend_ %s .png' % (mode))


























    