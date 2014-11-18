import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def histp(income_t,year):
    year=str(year)
    x=income_t.ix[year,:]
    x.hist(bins=70)
    plt.ylabel('Number of countries')
    plt.xlabel('income per person')
    plt.title('Year of {}'.format(year)  )
    plt.savefig('histogram_of_income_vs_countries{}.png'.format(year)) 
    #plt.show()
def Boxplot(data):
    """
    box plot of data
    """
    data.boxplot('Income', by='Region')
    plt.ylabel('Income per person')
    plt.title('box plot')
    plt.savefig('box_plot_group_by_region.png')
def HistRegionplot(data):
    """
    group by region hist 
    """
    data.hist('Income', by = data['Region'], xrot= 80, xlabelsize = 10, ylabelsize = 10, bins = 20, figsize = [10,10])
    plt.title('hist plot')
    plt.savefig('histogram_of_group_by_region.png') 