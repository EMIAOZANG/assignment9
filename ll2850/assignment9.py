__author__ = 'leilu'

import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from package.function_and_exception import *

data1 = pd.read_csv('countries.csv', header=0, sep=',')
countries = pd.DataFrame(data1)
data2 = pd.read_excel('indicator.xlsx', header=0, sep=',')
income = pd.DataFrame(data2)

def main():
    print question2(income)
    graph_plot(income)
    for year in range(1999, 2004):
        income_year = merge_by_year(year)
        plt.figure()
        income_year.boxplot('Income', by='Region')
        plt.savefig('box_plot_trends %d' % year)

        income_year.hist('Income', by = income_year['Region'], xrot = 90, xlabelsize = 10, ylabelsize = 10, bins = 20, figsize = [10,10])
        plt.savefig('histograms_trends %d' % year)
    f = open('results.txt', 'w')#open a file to write the analysis
    f.write('According to the box plots though recent years, we can tell that the median income per person is very steady for each regions, '
            'but the income range for North America increases a lot.')
    f.write('According to the histograms, we can see that the income distribution becomes less even for Oceania')
    f.flush()

if __name__ == '__main__':
    main()
