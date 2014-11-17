import pandas as pd
import matplotlib.pyplot as plt
from pylab import *

def loadData():
    #load the data in
    countries = pd.read_csv('countries.csv')
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx')

    #transform the income data
    income = income.T
    income.columns = income.ix[0]
    income = income[1:]

    print countries.head(), income.head()
    return countries, income

def histYear(df, year):
    #plot income distribution of all countries in a certain year
    df.dropna()
    df.ix[year].hist(bins = 50)
    plt.ylabel('freq') 
    plt.xlabel('(income per person interval in {})'.format(year))
    plt.show()

def histRegion(df):
    #plot income distribution by region in histograph
    plt.figure()
    df.hist('Income', by = df['Region'], xrot = 90, xlabelsize = 5, ylabelsize = 5, bins = 20, figsize = [10,10])

def box(df):
    #plot income by region in box plot
    plt.figure()
    df.boxplot('Income', by = 'Region')
    plt.ylabel('income per person')


def merge_by_year(year):
    #merge the data into three columns: country, region and income
    countries, income = loadData()
    incomeYear = pd.DataFrame(income.ix[year])
    incomeYear['Country'] = list(incomeYear.index)
    mergeData = pd.merge(incomeYear, countries, how = 'inner', on= 'Country')
    mergeData.columns = ['Income', 'Country', 'Region']
    columns = ['Country', 'Region', 'Income']
    return mergeData[columns]

def main():
    countries, income = loadData()
    while True:
        try:
            year = int(raw_input('select a year for income in all countries'))
            histYear(income,year)
            break

        except KeyboardInterrupt:
            print 'terminated!'
            sys.exit()
        except:
            print 'year has to be between 1800 and 2012'
        continue
    while True:
        try:
            start = int(raw_input('explore the data: start year for income by region'))
            end = int(raw_input('explore the data: end year for income by region'))
            plottype = raw_input('Plot box or histogram?(b/h)')
            if plottype == 'b':
                for year in range(start, end):
                    box(merge_by_year(year))
                    plt.savefig('boxplot_%d.png' %(year))
                    print 'Done!'
            elif plottype == 'h':
                for year in range(start, end):
                    histRegion(merge_by_year(year))
                    plt.savefig('histplot_%d.png' %(year))
                    print 'Done!'

        except KeyboardInterrupt:
            print 'terminated'
            sys.exit()
        except:
            print 'year has to between 1800 and 2012'
        continue
if __name__ == '__main__':
    main()
    '''
    while the rest reigions remain reletively constant, Asian has seen great increase in overall GDP per person in the last few years
    '''
