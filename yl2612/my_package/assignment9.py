import pandas as pd
import matplotlib.pyplot as plt
from functions import *


def main():
    '''
    Generate my answers for assignment 9
    '''
    
    #Q1: Load the data sets
    countries = pd.read_csv('countries.csv')
    income = pd.read_csv('indicator gapminder gdp_per_capita_ppp.csv')
    
    #Q2: Transform the income data set
    trans_income = income.T
    print '---------------Q2: The head of the transformed data set---------------'
    print trans_income.head()
    
    #Q3: Display the distribution of income per person in 2000
    countries_income_hist(trans_income,'2000')
    
    #Q4: Merge the countries and income data sets for Year 2000
    print '-----------------Q4: The merged data sets-----------------'
    print merge_by_year('2010')
    
    #Q5:
    for year in range(2010,2013):
        Q5_hist(merge_by_year(str(year)))
        plt.savefig('histogram_income_by_regions_in_{}.png'.format(year))
        Q5_boxplot(merge_by_year(str(year)))
        plt.savefig('boxplot_income_by_regions_in_{}.png'.format(year))

if __name__ == '__main__':
    main()     
        
    
    
    
    