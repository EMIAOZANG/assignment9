'''
Created on Nov 17, 2014

@author: jiminzi
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from assignment9.plot import Boxplot, HistRegionplot,histp
from assignment9.merge import merge_by_year
def main():
    
    #read the countries from csv
    countries=pd.read_csv('countries.csv')
    #change the csv as DataFrame
    countries=pd.DataFrame(countries)
    #print head of countries
    print countries.head()
    countries_t=countries.set_index('Country')
    #load the GDP file
    income=pd.read_excel('GDPpercapitaconstant2000US.xlsx')
    #convert the file to data frame
    income=pd.DataFrame(income)
    #print head of income
    print income.head()
    
    # set the year as index
    income_t = income.set_index('Income per person (fixed 2000 US$)')
    #transform the dataset to year as row and countries as column
    income_t=pd.DataFrame.transpose(income)
    
    '''
    plot year gap distribution of given year 2000
    '''
    histp(income_t,2000)
    
    '''
    plot box and hist plots of recent years
    '''
    
    for year in range(2007,2012):
        Boxplot(merge_by_year(year))
        plt.savefig('boxplot_%d.png' %(year))
        HistRegionplot(merge_by_year(year))
        plt.savefig('hist_region_income_%d.png' %(year))
    '''
    there is a reslut txt to describe data
    '''
    result=open('result.txt','w')
    result.write('by the box plot:\n I find, Asia and South America has an increasing mean Gdp.\n')
    result.write('Europe has a decrease trend in recent 5 years\n generally speaking Europe and North America have higher GDP \n')
    result.write('\n')
    result.write('by histogram plt:\n the distribition for each region does not change obviously\n')
    result.write('asia and Africa both show a increasing GDP curve\n some countries with a high income, and major of countries with a low income')
    result.close()
if __name__ == '__main__':
    main()