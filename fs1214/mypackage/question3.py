'''
Created on 2014.11.16

@author: apple
'''
import pandas as pd
import sys
import matplotlib.pyplot as plt
from mypackage.exceptions import *

"""
For any input of year, plot the distribution of income per person
across all countries.
"""

#check whether the input of year is valid, if not raise exceptions.
def check_input_value(year):
    while True:
        try:
            intTarget = int(year)
        except ValueError:
            raise YearInputException()
        else:
            if intTarget < 1800 or intTarget > 2012:
                raise YearBoundException()
            else:
                return (intTarget)

#plot the distribution of income per person
def bestplot(df,year):
    year_value = check_input_value(year)
    df.ix[year_value].hist(bins=50)
    plt.ylabel('The Number of Countries')
    plt.xlabel('Income per person')
    plt.title('In Year {}'.format(year))
    plt.savefig('hist_income_{}'.format(year))
    
def question3(newincome):
    print 'Question3:'
    year = raw_input('Please enter the year between 1800 and 2012:')
    while True:
        try:
            bestplot(newincome,year)
            break
        except KeyboardInterrupt:
            sys.exit()
        except (YearInputException,YearBoundException) as error:
            print error
            year = raw_input('Please enter the year between 1800 and 2012:')
    
    print '-------------------'
