__author__ = 'leilu'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_csv('countries.csv', header=0, sep=',')
countries = pd.DataFrame(data1)
data2 = pd.read_excel('indicator.xlsx', header=0, sep=',')
income = pd.DataFrame(data2)
#print countries.head()


def transformation(df):
    df = df.T
    return df

def question2(df):
    income_trans = transformation(df)
    return income_trans.head()


def graph_plot(df):
    """
    this function will take two arguments: 1) a data frame and 2) a year from user
    then it will plot a histogram for a row of series with the index of the year given
    """
    try:
        year = raw_input("which year do you want to take a look?")
        gdp_year = transformation(df).ix[int(year)]
        gdp_year.hist(bins=50)
        plt.xlabel('Income per Person')
        plt.ylabel('Num of Countries')
        plt.title('Income per Person at %s' % year)
        plt.savefig('histogram')
    except ValueError:
        print "Sorry! You should input a valid integer. Try again"

def merge_by_year(year):
    """
    this function will merge the data countries and income by any given year
    :param: year
    :return: merged data set DataFrame with three columns titled 'country', 'Region', and 'Income'
    """
    col_to_merge = pd.DataFrame(income[year]).ix[1:]
    col_to_merge['Country'] = list(col_to_merge.index)
    merged = pd.merge(countries, col_to_merge, on='Country', how='inner')
    merged.columns = ['Country', 'Region', 'Income']
    return merged

