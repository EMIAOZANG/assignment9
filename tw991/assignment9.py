import pandas as pd
from supportingfunction import *


def merge_by_year(year):
    """
    merge the countries and income data in a given year
    a new dataframe will be returned with columns = ['Country', 'Region', 'Income']
    """
    countries = pd.read_csv('countries.csv')
    income = pd.read_excel('income_pps.xlsx')
    incomeTrans = income.T
    incomeTrans.columns = incomeTrans.ix[0]
    incomeTrans = incomeTrans[1:]
    country_income = pd.DataFrame(incomeTrans.ix[year])
    country_income['Country'] = list(country_income.index)
    country_income.index = range(0, len(country_income))
    country_region_income = pd.merge(country_income, countries, on='Country', how = 'inner')
    country_region_income.columns = ['Income', 'Country', 'Region']
    cols = ['Country', 'Region', 'Income']
    return country_region_income[cols]


def main():
    incomeTrans = question2()
    plotHist(incomeTrans, 2000)
    for year in range(2006,2012):
        plotBox(merge_by_year(year))
        plt.savefig('boxplot_%d.png' %(year))
        plotHistRegion(merge_by_year(year))
        plt.savefig('hist_region_income_%d.png' %(year))
    #Asia enjoys an increase in income per person over last few years. Europe and North America see a decreasing gap
    # between the rich and the poor

if __name__ == '__main__':
    main()