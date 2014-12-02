'''
Created on Nov 10, 2014

@author: luchristopher
'''
from getdata import *
from gdp import *
from superio import safeInput
from utilities import *


def main():
    countries, income = getData()
    income_info = PerCapitaGDP(income,countries)
    year = safeInput('Please input the year:\n',['exit','quit'],year_parser)
    income_info.plotIncomeHistByYear(year)
    income_info.plotIncomeBoxByYear(year)
#     years = safeInput('Please Input a series of years:\n',['exit','quit'],years_parser)
#     income_info.mergeByYears(years)
#     income_info.describeBy('Region', years)

if __name__ == '__main__':
    main()