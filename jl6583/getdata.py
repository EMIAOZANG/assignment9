'''
Created on Nov 10, 2014

@author: luchristopher
'''
import sys
import pandas as pd
import numpy as np

def getData():
    '''
    gets data from the specified csv file with exception handling regime
    '''
    try:
        countries = pd.read_csv('countries.csv')
    except:
        print >> sys.stderr, 'FAILURE : Cannot import data from file!\n'

    try:
        income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col='gdp pc test').transpose()
    except:
        print >> sys.stderr, 'FAILURE : Cannot import data from file!\n'
    print countries, income
    return countries, income
    
    
    