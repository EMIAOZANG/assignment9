__author__ = 'chianti'


from funcs_assign9 import *



def main():

    # For example: set year=1999 to check the distribution of income in 1999
    # Change this to whatever year you want from 1820 to 2012, inclusive.
    year = 1999

    if 1 == 1:
        # Let the user type in a year, this part displays a plot showing the distribution of income per person across
        # all countries in the world for the given year
        PlotDistribution(year)

    if 2 == 2:
        # This part merges the countries and income data sets for any given year.
        # The result should be a DataFrame with three columns titled Country, Region, and Income
        merge = merge_by_year(year)


    if 3 == 3:
        # This part uses bar plots and box plots to show the distribution of the income per person by region,
        # for a given year

        PlotByRegion(merge)

        PlotBoxPlotByRegion(merge)






if __name__ == '__main__' and True:
    main()
