import pandas as pd
import matplotlib.pyplot as plt


def question2():
    income = pd.read_excel('income_pps.xlsx')
    incomeTrans = income.T
    incomeTrans.columns = incomeTrans.ix[0]
    incomeTrans = incomeTrans[1:]
    print incomeTrans.head()
    return incomeTrans


def plotHist(dataframe, year):
    """display histogram for dataframe in year"""
    dataframe.ix[year].hist(bins=60)
    plt.ylabel('Number of countries')
    plt.xlabel('income per person')
    plt.title('Year of %d' % (year))
    plt.savefig('hist_income_person.png')


def plotBox(dataframe):
    """plot Boxplot for dataframe"""
    plt.figure()
    dataframe.boxplot('Income', by='Region')
    plt.ylabel('Income per person')


def plotHistRegion(dataframe):
    """plt histogram for dataframe group by region"""
    plt.figure()
    dataframe.hist('Income', by = dataframe['Region'], xrot= 90, xlabelsize = 10, ylabelsize = 10, bins = 20, figsize = [10,10])