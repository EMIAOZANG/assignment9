'''
Created on 2014.11.16

@author: apple
'''

import matplotlib.pyplot as plt
from mypackage.question4 import *

#use histogram and boxplot to explore the distribution of the income per person by region 
def exploreplot(tool,year):
    df_year = merge_by_year(year)
    if tool == 'boxplot':
        df_year.boxplot('Income',by='Region')
        plt.title('Boxplot of income per person by region in {}'.format(year))
        plt.xlabel('Region')
        plt.ylabel('Income per person')
        plt.savefig('boxplot_incomebyregion_{}'.format(year))
    elif tool == 'histogram':
        df_year.hist('Income',by=df_year['Region'],bins=20, xrot=100, figsize = [10,10])
        plt.savefig('hist_incomebyregion_{}'.format(year))
   

def question5():
    print 'Question5:'
    for year in range(2008,2013):
        exploreplot('boxplot',year)
        exploreplot('histogram',year)
    #plot the changes in these recent five years and compare the graphs.
    #write a txt to describe the changes in these recent years.
    f = open('describechanges.txt','w')
    f.write('From the boxplot, in recent years, income per person in Asia and south America has increased. And income per person in Europe has a decreasing trend.\n'
            'From the histogram,the distribution of each region generally remains the same. The lower income per person in Europe and North America has increased, decreasing the gap between the upper income and lower income.')
    
    print '-------------------'