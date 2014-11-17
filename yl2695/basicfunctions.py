import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def problem2():
    '''
    Transform the data set income to have years as the rows and countries as the columns. Show the
head of this data set when it is loaded.
    '''
    # read the file
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx')

    # let the dataframe has years as rows and countries as columns
    column = list(income['gdp pc test'])
    row = list(income.columns[1:])
    income = pd.DataFrame(np.array(income[income.columns[1:]]).T, columns=column, index=row)

    # show the head of the data set
    print income.head()
    return income


def display(year):
    '''
    Using histogram to display the distribution of income per person across all countries in the world for
any given year.
    '''
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx')
    column = list(income['gdp pc test'])
    row = list(income.columns[1:])
    income = pd.DataFrame(np.array(income[income.columns[1:]]).T, columns=column, index=row)

    # use histogram to show the distribution and save the picture
    plt.figure()
    plt.hist(income.ix[year].dropna(), bins=100)
    plt.xlabel('Income Per Person')
    plt.ylabel('Number of Countries')
    plt.title('The Year of {}'.format(year))
    plt.savefig('The Year of {}'.format(year))


def merge_by_year(year):
    '''
    This function merges the countries and income data sets for any given year. The result is a DataFrame with three columns titled 'Country', 'Region', and 'Income'.
    '''
    countries = pd.read_csv('countries.csv')
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx')
    income = income.rename(columns={'gdp pc test': 'Country'})
    country_income = pd.DataFrame

    # meger the two dataframes and delete the NaN data
    country_income = income[["Country", year]].merge(countries, on='Country', how='left')
    country_income = country_income.rename(columns={year: 'Income'})
    country_income = country_income[['Country', 'Region', 'Income']]
    country_income = country_income.dropna()
    country_income.index = range(len(country_income))
    return country_income


def boxplot(dataframe):
    '''
    plot boxplots of the income and region of a given year.
    '''
    plt.figure()
    dataframe.boxplot('Income', by='Region')
    plt.ylabel('Income Per Person')


def histgram(dataframe):
    '''
    plot histograms of the income and region of a given year.
    '''
    plt.figure()
    dataframe.hist('Income', by='Region', bins=50)
    plt.ylabel('Number of Countries')
