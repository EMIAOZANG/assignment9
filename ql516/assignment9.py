# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 14:11:18 2014

@author: LaiQX
"""
from functions import *
from exception_list import *
    
def main():
    countries, income = read_data()
    
    while 1:
        year = raw_input("Input a year (from 1800 to 2012) of which you want to see the income distribution: ")    
        try:
            income_distribution_plot(income, year)
            break
        except year_out_of_range:
            print "please input a year in the range of [1800, 2012]"
        except not_a_valid_year:
            print "please input number as the year number between 1800 and 2012"


    print "plot histograms or boxplot to explore the income of year:  "
    while 1:
        explore_year = raw_input('input a year from 1800 to 2012:')
        try:
            data_year = merge_by_year(countries, income, explore_year)
            break
        except year_out_of_range:
            print "please input a year in the range of [1800, 2012]"
        except not_a_valid_year:
            print "please input number as the year number between 1800 and 2012" 


    while 1: 
        plot_mode = raw_input(r'choose to plot histograms(h) or boxplot(b) [h/b]' )    
        try:
            data_explore(data_year, explore_year, plot_mode)
            break
        except year_out_of_range:
            print "please input a year in the range of [1800, 2012]"
        except not_a_valid_year:
            print "please input number as the year number between 1800 and 2012" 
        except invalid_plot_mode:
            print "please seclect a valid mode from [b/h] "
    

    print "show the trend of recent year (to 2012)"    
    while 1:
        year_begin = raw_input("Year start at: ")
        try: 
            year_begin=int(year_begin)
            if year_begin>2011 or year_begin<1800 :
                raise year_out_of_range
            break
        except ValueError:
            print "please input a valid year (between 1800 - 2011)"
        except year_out_of_range:
            print "please input a valid year (between 1800 - 2011)"
    
    while 1:
        try:
            plot_mode = raw_input(r'choose to plot mode [mean,max,min,median]: ' )
            if not(plot_mode in ['mean','max','min','median']):
                raise invalid_plot_mode
            break
        except invalid_plot_mode:
            print "please choose a plot mode from these options:mean,max,min,median "
    
    trend_plot(countries, income, plot_mode,year_begin)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

