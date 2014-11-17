
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def initializing():
    '''
    Return the matrix in question2, which is the transpose of the original 'income' file
    :return: income Transpose
    '''
    income = pd.read_excel("income.xlsx")
    incomeT = income.transpose()
    incomeT.columns = incomeT.ix[0]
    incomeT = incomeT[1:]

    print incomeT.head()
    return incomeT
    
def merge_by_year(year):
    '''
    merge fuctions: takes any year's income from 'income and merge with 'countries.csv' into a new data frame
    :param year:
    :return:'merge' dataframe
    '''
    income = pd.read_excel("income.xlsx")
    income = income.set_index('gdp pc test')

    countries = pd.read_csv("countries.csv")

    incomeSeries = income[year]
    listofCountries = [country for country in countries['Country']]
    listofIncome = []
    for country in listofCountries:
        if country in incomeSeries.index:
            listofIncome.append(incomeSeries[country])
        else:
            listofIncome.append(np.NaN)
    merge = countries
    merge['Income'] = listofIncome

    return merge

def plotHistagram(dataframe, year):
    '''
    plot the graph for income per entity for all countries on 2000,
    which has income on x and the corresponding number of countries on y
    '''
    dataframe.ix[year].hist(bins=60)
    plt.ylabel("number of countries")
    plt.xlabel("income per entity")
    plt.savefig("income_per_entity_across_countries.png")

def plotBoxPlot(dataframe,year):
    '''
    Plot the box plot graph for regional income, with income on x and
    number of countries on the y-axis
    '''
    dataframe.boxplot('Income', by='Region')
    plt.ylabel("Income per entity")
    plt.savefig("Box Income_by_region of year %d" %(year))

def plotHista(dataframe,year):
    '''
    Plot the histogram for regional income for analytical purpose,
    axis seen above
    '''
    dataframe.hist('Income', by=dataframe['Region'], xlabelsize = 7)
    plt.xlabel("Income per entity")
    plt.ylabel("Number of countries")
    plt.savefig("Histogram Income_by_region of year %d" %(year))

if __name__ == "__main__":
    income = initializing()
    plotHistagram(income, 2000)
    for year in range(2007,2013):
        merge = merge_by_year(year)
        plotBoxPlot(merge,year)
        plotHista(merge,year)

'''
The graphs from recent year indicate that the income gap per region has decreased over the years, yet oceania
region pertains to a decreasing income level,while the overall level for other regions remain rather constant.
The histogram graphs show that there's a tendency that the number of low-income has decreased. However the number of
entities that at high-income level does not increase.
'''



    
    
    
    