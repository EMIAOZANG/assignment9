'''
Created on 2014.11.16

@author: apple
'''

import pandas as pd
import sys
import matplotlib.pyplot as plt
from mypackage.question3 import *
from mypackage.exceptions import *

#merge the countries and income data sets for any given year
def merge_by_year(year):
    #check whether the input of year is valid
    year_value = check_input_value(year)
    
    countries = pd.read_csv('countries.csv')
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx')
    income = income.rename(columns={'gdp pc test':'Country'})
    #get the data of income in that year
    income_year = income[['Country',year_value]]
    merge = pd.merge(countries,income_year,how = 'inner')
    merge = merge.rename(columns={year_value:'Income'})
    return merge

def question4():
    print 'Question4:'
    year = raw_input('Please enter the year between 1800 and 2012:')
    while True:
        try:
            merge = merge_by_year(year)
            print merge.head()
            break
        except KeyboardInterrupt:
            sys.exit()
        except (YearInputException,YearBoundException) as error:
            print error
            year = raw_input('Please enter the year between 1800 and 2012:')
    
    print '-------------------'
