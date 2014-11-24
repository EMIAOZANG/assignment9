'''
Created on Nov 18, 2014

@author: keye
'''

import pandas as pd
import matplotlib.pyplot as plt

def load_dataset():
    """
    Load the countries.csv file into a pandas DataFrame and name this data set countries;
    Load the 'Income per person' data set into a DataFrame called income.
    """

    countries = pd.read_csv('countries.csv')
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col='gdp pc test')
    return countries, income   

def plot(year):
    """
    Display the distribution of income per person across all countries in the world for any given year(e.g. 2000).
    """
    
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col='gdp pc test')
    plt.figure()
    income_transformation = income.T
    annual_income = income_transformation.ix[year].dropna()
    annual_income.hist(bins=80,color='red')
    plt.ylabel('Number of countries')
    plt.xlabel('Income per person')
    plt.title('Income per Person of Year {}'.format(year))
    plt.savefig('Income per Person of Year {}'.format(year))

def merge_by_year(year):
    """
    Create a function to merge the countries and income data sets for any given year. 
    The result is a DataFrame with three columns titled 'Country', 'Region', 'Income'
    """
     
    #Load the data sets.
    countries = pd.read_csv('countries.csv')
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx')
    #Change the name of 'gdp pc test' to 'Country'
    income = income.rename(columns={'gdp pc test':'Country'})
    annual_country_income = income[['Country',year]].merge(countries, on='Country', how='left')
    annual_country_income = annual_country_income.rename(columns={year:'Income'})
    annual_country_income.columns=['Country', 'Income', 'Region']
    return annual_country_income

def histograms(df):
    """
    Create histograms of the income and region of a given year.
    """
    
    plt.figure()
    df.hist('Income',by=df['Region'], bins=40, xrot=60, xlabelsize=6)
    plt.ylabel('Number of Countries')
    plt.xlabel('Income per Person')

def boxplots(df):
    """
    Plot boxplots of the income and region to explore the distributions.
    """
    
    plt.figure()
    df.boxplot('Income', by='Region')
    plt.ylabel('Income per Person')
    plt.xlabel('Region')

def analysis():
    """ 
    Create a file to write down the description of changes in the recent years.
    """
    
    analysis = open('analysis.txt','w')
    analysis.write('From the boxplots of the recent 6 years (2007-2012), we can see that the income per person in Asia and South America has increased while the income per person in North America and Europe is decreasing.\nThe distribution of the income per person by each region generally remains the same as shown in the histograms. \n') 