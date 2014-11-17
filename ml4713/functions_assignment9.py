# -*- coding: utf-8 -*-
"""Functions file
   Mengfei Li
"""
import pandas as pd
import numpy as np


def data_input():
    global col,countries,income
    countries=pd.read_csv('/Users/mengfeili/countries.csv')
    income=pd.read_excel('/Users/mengfeili/Downloads/gdp.xlsx')
    col=income['gdp pc test']
    ind=income.columns[1:]
    income=pd.DataFrame(income.drop('gdp pc test',1).values.T,columns=col,index=ind)
    print "Income and Countries Data Loaded"
    return countries,income,col,ind
    
        
def merge_by_year(year):
    """Merge countries and income two datasets according to a specified year
       Match country names with respect to two data frames.
       Take a year as an input and return the merged dataframe.
       Warning:
       the income dataset is different from the original dataset. The one used in 
       this function is transposed already, i.e. columns are country names and rows 
       are years.
    """
    #select country names that exist in both datasets
    sel=[]
    for elem in col:
        if elem in set(countries.Country):
           sel.append(elem)
        else:
           continue
      
    countries['new_col']=countries.Country
    countries_new=countries.set_index(countries.new_col).drop('new_col',1)  
    
    #selecting income across countries in the year specified by user
    income_selected=income[sel]
    year_income=income_selected.ix[year]
    year_income.index=sel
    year_income.name='Income'
    
    #merge two data frames
    merged_df=pd.merge(countries_new,pd.DataFrame(year_income),how='outer',right_on=None,left_on=None,left_index=True,right_index=True)
    merged_df=merged_df.set_index(np.arange(194))

    return merged_df
    

