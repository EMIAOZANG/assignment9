import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def merge_by_year(year):
    '''
    It is a function which I use to get a new dataframe with column 'Country','region', and 'income'
    by each year
    '''
    #set the year as string to use when ix a column
    year=str(year)
    countries=pd.read_csv('/users/jiminzi/git/2014_data/countries.csv')
   #change the csv as DataFrame
    countries=pd.DataFrame(countries)
    countries_t=countries.set_index('Country')
   #load the GDP file
    income=pd.read_excel('/Users/jiminzi/Downloads/GDPpercapitaconstant2000US.xlsx')
   #convert the file to data frame
    income=pd.DataFrame(income)
    #'Set the data with Index Country'
    income['Country']=income['Income per person (fixed 2000 US$)']
    incomes=income.drop(['Income per person (fixed 2000 US$)'],1)
    income_merge=incomes.set_index('Country')   
    #merge country and Income by the Index 'Country'
    df1=pd.merge(countries_t,income_merge, left_index=True, right_index=True,how='inner')
    #get data from my merge dataframe
    newdf=df1.ix[:,['Region',year]]  
    #set a column named country from my index
    newdf['Country'] = newdf.index
    #change the colume name from year to Income
    newdf=newdf.rename(columns = {year:'Income'})
    #newdf['Country'] = newdf.index
    newdf.index = range(len(newdf))
    #change the order of columns to 'Country' ,'Region','Income'
    cols = ['Country', 'Region', 'Income']
    data = pd.DataFrame(newdf, columns = cols)
    return data