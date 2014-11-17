__author__ = 'chianti'

import pandas as pd
import matplotlib.pyplot as plt


# Load the countries.csv file into a DataFrame and name this data set countries
countries = pd.read_csv('countries.csv')

# This function loads 'indicator gapminder gdp_per_capita_ppp.xlsx' into a DataFrame,
# transforms the data set and shows the head of it when it is loaded
def LoadAndTransform():

    income = pd.io.excel.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx')
    income.fillna(0, inplace=True)
    # Load 'indicator gapminder gdp_per_capita_ppp.xlsx' into a DataFrame
    # Fill the NaN values with 0

    Transed_income = income.T
    Transed_income.columns = Transed_income.ix[0]
    # Transform the data set and let countries be the columns

    final_income = Transed_income.ix[1:]
    # Delete the repeated first row

    print 'The data set is loaded. \nHere is the head of it:'
    print final_income.head()

    return final_income


# Load 'Income per person (GDP/capita, PPP$ inflation-adjusted)' data set into a DataFrame
# Transform the data set to have years as the rows and countries as the columns.
# Show the head of this data set when it is loaded.
income = LoadAndTransform()


# This function is supposed to be used after using LoadAndTransform()
# Set data = LoadAndTransform()
# PlotDistribution(data) will let the user type in a the given year (e.g. 2000) and then display the distribution of
# income per person across all countries in the world for the given year .
def PlotDistribution(year):


    year_Income = income.ix[year]

    fig, axes = plt.subplots(2, 1)

    year_Income.hist(bins=100, alpha=.4, color='r', ax=axes[1])
    axes[0].set_title('Income per person in the world in '+str(year)+' (bins=100)')

    year_Income.hist(bins=50, alpha=.4, color='r', ax=axes[0])
    axes[1].set_title('Income per person in the world in '+str(year)+' (bins=50)')

    axes[0].set_ylabel('Number of countries')
    axes[1].set_ylabel('Number of countries')

    axes[0].set_xlabel('Income per person')
    axes[1].set_xlabel('Income per person')

    plt.subplots_adjust(wspace=0, hspace=0.6)

    plt.savefig('PlotDistributionByYear.png')
    plt.show()

# This function merges the countries and income data sets for any given year.
# The result should be a DataFrame with three columns titled Country, Region, and Income
def merge_by_year(year):

    merge = pd.merge(countries, income.T, how="inner", left_on='Country', right_on=income.T.index)
    # merge two data sets

    selected = merge[['Country', 'Region', year]]
    #choose the merged data set according to a given year

    selected.columns = ['Country', 'Region', 'Income']
    # rename the name of the year column to be 'Income'

    return selected




# This function will plot six plots for each region, showing the distribution of income per person in each region
def PlotByRegion(merge):

    fig, axs = plt.subplots(3, 2, facecolor='w', edgecolor='k')
    fig.subplots_adjust(hspace=.5, wspace=.5)

    axs = axs.ravel()

    i = 0

    for each_Region in set(merge.Region):


        axs[i].hist(list(merge[merge.Region == each_Region].Income), bins=20)

        for tick in axs[i].xaxis.get_ticklabels():
            tick.set_fontsize(9)
            tick.set_rotation(30)

        axs[i].set_title('Income per person in {}'.format(each_Region))

        i += 1


    plt.savefig('BarPlotByRegion.png')
    plt.show()

# This function will plot a bar plot to show the distribution of income per person in each region, for a given year
def PlotBoxPlotByRegion(merge):

    regions = sorted(set(merge.Region))
    data_to_plot = [list(merge[merge.Region == each_region].Income) for each_region in regions]

    fig = plt.figure(1, figsize=(9, 6))
    ax = fig.add_subplot(111)

    plt.boxplot(data_to_plot)

    ax.set_xticklabels(regions)

    plt.xlabel('Region')
    plt.ylabel('Number of people')
    plt.title('Income per person')

    plt.savefig('BoxPlotByRegion.png')
    plt.show()


