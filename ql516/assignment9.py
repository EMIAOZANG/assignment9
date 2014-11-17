# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 14:11:18 2014

@author: LaiQX
"""
from functions import *

    
def main():
    
    countries,income = read_data()

    year=int(raw_input("Input a year (from 1800 to 2012) of which you want to see the income distribution: "))
    income_distribution_plot(income,year)
    
    print "plot histograms or boxplot to explore the income of year:  "
    explore_year=int(raw_input('input a year from 1800 to 2012:'))    
    plot_mode= raw_input(r'choose to plot histograms(h) or boxplot(b) [h/b]' )
    data_year = merge_by_year(countries,income,explore_year)
    data_explore(data_year,explore_year,plot_mode)
    
    print "show the trend of recent year (to 2012)"    
    year_begin = int(raw_input("Year start at: "))
    plot_mode= raw_input(r'choose to plot mode [mean,max,min,median]: ' )
    trend_plot(countries,income,plot_mode,year_begin)


if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

