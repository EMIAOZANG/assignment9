'''
Created on Nov 18, 2014

@author: keye
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functions import *


def main():
    
    #Question 1: Load the data sets 'countries' and 'income'.
    print '--------Question 1--------'
    print 'Load the coutries.csv into a data set "countries".' +'\n' +'Load the "Income per person" into a data set "income". \n'
    countries,income = load_dataset()
    print 'Finished! \n'
    print '----------------------------------------------------------------------- \n'
    
    #Question 2: Transform the data set 'income' and show the head of this data set.
    print '--------Question 2--------'
    income_transformation = income.T
    print 'The head of the data set "income" after transforming is \n'
    print income_transformation.head() 
    print '----------------------------------------------------------------------- \n'
    
    #Question 3: Display the distribution of income across all countries for any given year(e.g. 2000).   
    print '--------Question 3--------'
    try:
        year = raw_input('Input a year: ')
        print 'Question 3: Display the distribution of income per person across all countries in the world for {} :\n'.format(year)
        plot (int(year))
    except:
        print 'Your input is invalid!!' 
    print '----------------------------------------------------------------------- \n'

    #Question 4: Use the function merge_by_year(year) to merge the countries and income data sets for any given year.  
    print '--------Question 4--------'
    try:
        year = raw_input('Input a year: ')  
        print 'Question 4: Merge the countries and income data sets for {}: \n'.format(year)
        print merge_by_year(int(year))
    except:
        print 'Your input is invalid!!' 
    print '----------------------------------------------------------------------- \n'
    
    #Question5: Use exploratory data analysis tools to explore the distribution of the income by region data set for a given year. And describe their changes of the recent years.
    print '--------Question 5--------'
    print 'Question 5: Explore the distribution of the income per person by region data set from year 2006 to 2012: \n'
    #Plot the changes from 2008 to 2012 and compare them. 
    for year in range(2007,2013):
        histograms(merge_by_year(int(year)))
        plt.savefig('histogram for year {}'.format(year))
        boxplots(merge_by_year(int(year)))
        plt.savefig('boxplot for year {}'.format(year)) 
    analysis()  
    
if __name__ == '__main__':
    main()
