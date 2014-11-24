'''
Created on Nov 18, 2014

@author: keye
'''
import sys
import pandas as pd
import matplotlib.pyplot as plt
from functions import *
from Exceptions import *

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
    print 'The head of the data set "income" after transforming is: \n'
    print income_transformation.head() 
    print '----------------------------------------------------------------------- \n'
    
    #Question 3: Display the distribution of income across all countries for any given year(e.g. 2000).   
    print '--------Question 3--------'
    while True:
        try:
            #Input an integer to be a year value.
            year = eval(raw_input('Input a year: '))
            #Check if the input is an integer. If not, raise an exception and input again.
            if type(year) != int:
                raise InvalidYearValue()
            #Check if the input is between 1800 and 2012. If not, raise an exception and input again.
            elif year<1800 or year>2012:
                raise InvalidYearRange()
            break
        except (KeyboardInterrupt,EOFError):
            print '\nYou are going to exit the program.\nBye!'
            sys.exit()
        except (InvalidYearValue,SyntaxError,NameError):
            print 'Oops! The input is not a valid year value! You should input an integer! Please try again.'
        except InvalidYearRange:
            print 'Oops! The input year value should be in the range of 1800 to 2012! Please try again.'
    print 'Question 3: Display the distribution of income per person across all countries in the world for {} :\n'.format(year)
    #Creat the plot of the distribution(income per person across all countries) for any given year between 1800 and 2012.
    plot (year) 
    print '\nFinished!'
    print '----------------------------------------------------------------------- \n'

    #Question 4: Use the function merge_by_year(year) to merge the countries and income data sets for any given year.  
    print '--------Question 4--------'
    while True:
        try:
            #Input an integer to be a year value.
            year = eval(raw_input('Input a year: '))
            #Check if the input is an integer. If not, raise an exception and input again.
            if type(year) != int:
                raise InvalidYearValue()
            #Check if the input is between 1800 and 2012. If not, raise an exception and input again.
            elif year<1800 or year>2012:
                raise InvalidYearRange()
            break
        except (KeyboardInterrupt,EOFError):
            print '\nYour are going to exit the program.\nBye!'
            sys.exit()
        except (InvalidYearValue,NameError,SyntaxError):
            print 'Oops! The input is not a valid year value! You should input an integer! Please try again.'
        except InvalidYearRange:
            print 'Oops! The input year value should be in the range of 1800 to 2012! Please try again.'
    print 'Question 4: Merge the countries and income data sets for {}: \n'.format(year)
    #Merge the countries and income data sets for any given year between 1800 and 2012.
    print merge_by_year(year) 
    print '\nFinished!'
    print '----------------------------------------------------------------------- \n'
    
    #Question5: Use exploratory data analysis tools to explore the distribution of the income by region data set for a given year. And describe their changes of the recent years.
    print '--------Question 5--------'
    print 'Question 5: Explore the distribution of the income per person by region data set from year 2007 to 2012: \n'
    #Plot the changes from 2008 to 2012 and compare them. 
    for year in range(2007,2013):
        histograms(merge_by_year(year))
        plt.savefig('histogram for year {}'.format(year))
        boxplots(merge_by_year(year))
        plt.savefig('boxplot for year {}'.format(year)) 
    #Write a description of the changes(distribution of the income per person by region) through the recent years.
    analysis()  
    print '\nFinished!'
    
if __name__ == '__main__':
    main()
