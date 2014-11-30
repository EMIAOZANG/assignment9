import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.mpl_style', 'default')
import matplotlib.pylab as pylab
pylab.rcParams['figure.figsize'] = (16.0, 10.0)


def main():
    # Question 1&2
    countries = pd.read_csv('countries.csv')
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col=0).T
    print income.head()


    # Question 3
    def display(year):
        '''This function plots histogram of the income distribution for a given year
        
        '''
        data = income.ix[year].dropna().hist(bins=100)
        plt.title('Income Distribution of Year {}'.format(year))
        plt.xlabel('US$ Income per Person')
        plt.ylabel('Number of Countries')
        plt.savefig('Hist_{}'.format(year))

    display(2000)

    # Question 4
    def merge_by_year(year):
        '''This function merges the income information with the country and region information for a given year. 
    
        Returns a data frame with 3 columns titled 'Country', 'Region', and 'Income' separately.'''
        tmp = pd.DataFrame(income.ix[year])
        tmp['Country'] = list(tmp.index)
        Merged_DF = countries.merge(tmp, on='Country')
        Merged_DF.columns = ['Country', 'Region', 'Income']
        return Merged_DF

    merge_by_year(2009)

    # Question 5

    # Plot box-plots and histograms to explore the income changes from 2009 to 2012
    # The description of the results is in 'Result_Description.txt'
    for i in range(2009,2013):
        plt.figure()
        merge_by_year(i).boxplot('Income', by='Region')
        plt.savefig('boxplot_{}'.format(i))
        plt.figure()
        merge_by_year(i).hist('Income', by='Region')
        plt.savefig('hist_region_{}'.format(i))


if __name__ == '__main__':
    main()