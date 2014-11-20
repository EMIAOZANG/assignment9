import pandas as pd
import sys
from package.exceptions import *
from package.functions import *

"""Goal of program is to use exploratory data tools (histograms and boxplots) to generate graphical displays for:
    1. income distribution per person across all countries in the world, and
    2. income distribution per person by region data set
    for a user-inputted year.
Observe how these change through recent years."""

def main():
    #Question 1. load data sets: countries and income
    countries = pd.read_csv('countries.csv')
    income = pd.read_excel('income.xlsx',sheetname='Data')
    trans_income = transform_dataset(income)
    income_head = trans_income.head()
    print 'Question 2. \nPrinting head of transformed data set: \n'
    print income_head

    while True:
        try:
            #obtain user input for year to be analyzed
            year = raw_input('Please input year between 1800 and 2012: ')
        except KeyboardInterrupt:
            print 'Keyboard Interrupt. Bye!'
            sys.exit()
        if year.lower() == 'quit':
            print 'Quit. Bye!'
            sys.exit()
        else:
            try:
                valid_year = isValidYear(year)
                print 'Generating results for ' + str(valid_year) + '\n'
                break
            except notValidYearError:
                print 'Not a valid year. Must be integer between 1800 and 2012 (inclusive).'
                
    #Question 3. Graph histogram of income per person across all countries in the year 2000 (user input)
    try:    
        graph_all_countries(trans_income, valid_year)
    except:
        print 'Cannot graph all countries plot'
    
    try:
        merged = merge_by_year(countries, income, valid_year)
    except:
        print 'Cannot merge'
        
    try:
        for year in range(2004, 2013):
            region_histogram(merge_by_year(countries,income,year), year)
    except:
        print 'Cannot plot regional histogram'     
        
    try:
        for year in range(2004, 2013):
            region_boxplot(merge_by_year(countries,income,year), year)
    except:
        print 'Cannot plot regional boxplot'
        
    

if __name__=='__main__':
    main()
    