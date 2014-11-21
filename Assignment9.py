
#############################
#                           #
#       Assignment 9        #
#       Maya Rotmensch      #
#                           #
#############################

from pylab import rcParams
from collections import defaultdict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

""" Formatting for doc strings was done according to google style guide https://google-styleguide.googlecode.com/svn/trunk/pyguide.html"""

def loadData():
    countries = pd.read_csv("countries.csv")
    income_initial = pd.ExcelFile("indicator gapminder gdp_per_capita_ppp.xlsx")
    dfs = {sheet_name: income_initial.parse(sheet_name) 
              for sheet_name in income_initial.sheet_names}

    income = dfs['Data'] # we only care about the sheet containing the data
    income_transformed = income.set_index("gdp pc test").T
    return countries, income_transformed 


def incomeDistribution(year):
    """ Graphes the income distribution for a given year.
    ignores missing (Nan) values

    Args:
        year: the year for which the distribution is calculated. must be inputed in int form (not string!).
        
    Returns:
        saves .png of distribution.
    """
    
    rcParams['figure.figsize'] = 15,7
    income_for_given_year = income.ix[year]
    plottable_values = income_for_given_year[income_for_given_year.notnull()]
    
    plt.hist(plottable_values, bins = 50)
    plt.title("Distribution of income across countries \n for the year %s" %year)
    plt.xlabel("Income per person")
    plt.ylabel("Counts")
    plt.savefig("incomeDistribution for %s" %year)
    plt.show()
    return

def merge_by_year(year, all_infomation_present = True):
    """ Merges the income and countries DataFrames for a given year.
    Columns are 'Country', 'Region', and 'Income'. 

    Args:
        year: int. the year for which the distribution is calculated.
        all_infomation_present: boolean. If true performs inner join. 
                If false performs outer join and keeps all rows with partial information (will discard rows with missing information for both region and income fields)
        
    Returns:
        merged_2 : a merged pandas DataFrame for the given year.
     """
    
    countries_shifted_index = countries.set_index('Country')
    income_given_year = income.ix[year]

    if all_infomation_present == True:
        merged = pd.concat([countries_shifted_index,income_given_year], axis = 1, join = "inner")
    else:
        merged = pd.concat([countries_shifted_index,income_given_year], axis = 1, join = "outer")
        merged  = merged.dropna(how = "all") #drop rows with no information of region and income.
    
    merged_2 = merged.reset_index(level=0)
    merged_2.columns = ['Country', 'Region', 'Income']
    return merged_2

def incomeOverTime(country):
    """ graphs change in the income per person for a given country over time. 
    ignores missing information. 
    
    Args:
        country: string. country for which the analysis is performed.

    Returns:
        save .png of change of Income over time. 

    Raises:
        NotEnoughInformation: If less than less than 2 information points. 
        
    """
    country_income_timeline = income[country]
    income_not_null = country_income_timeline[country_income_timeline.notnull()]
    
    if len(income_not_null>2): # must have more than 2 points to plot
        plt.plot(income_not_null.index,income_not_null)
        plt.xlabel("Year")
        plt.ylabel("Income")
        plt.xlim((income_not_null.index[0],income_not_null.index[-1]))
        plt.title("Change of Income over time in %s" %country)
        plt.savefig("Change of Income over time in %s.png" %country)
        plt.show()
    
    return


def distributionOfIcomeByRegion(year):
    """Graphes the distribution of income per person by region. ignores null values.

    Args: 
        year: int. the year for which the analysis will be performed.

    Returns:
        6 sub plots (all histoggrams) depicting the distribution of income for region by year.
        note that the distributions are normalized.
        saves plot grid as .png
    """
    merged = merge_by_year(year) #get info for year
    
    regions = countries.Region.unique()
    regions = np.array(regions).reshape(3,2)
    
    f, axarr = plt.subplots(regions.shape[0], regions.shape[1]) #create grid
    
    #populate subplots.
    for i in range(regions.shape[0]):
        for j in range(regions.shape[1]):
            r = regions[i,j]
            income_per_region = merged.Income[merged.Region== regions[i,j]]
            income_not_null = income_per_region[income_per_region.notnull()]
            axarr[i, j].hist(income_not_null.values, bins = 20, normed = True)
            axarr[i, j].set_title("Distribution of income for %s in year %s" %(str(regions[i,j]),year))

            
    plt.tight_layout()
    plt.savefig("Distribution of income for %s in year %s" %(str(regions[i,j]),year))
    plt.show()
    return

    

def MeanIncomeOverTime(region):
    """Plots the mean income per person in a given region over time. 
     analysis ignores null values.

    Args: 
        region: string. the region for which the analysis will be performed.

    Returns:
        a graph of the change in income over time. plot saved as .png
    """   

    over_time = []
    
    #calculate mean income per person in region for given year
    for i in income.index:
        merged = merge_by_year(i)
        income_per_region = merged.Income[merged.Region== region].mean()
        over_time.append(income_per_region)
    
    plt.plot(income.index,over_time)
    plt.xlabel("Year")
    plt.ylabel("Income")
    plt.xlim((income.index[0],income.index[-1]))
    plt.title("Change of Income over time in %s" %region)
    plt.savefig("Change of Income over time in %s" %region)
    plt.show()
    return 


def MeanIncomeOverTimeAllRegions():
    """ Plots the mean income per person in a given region over time. ovelays the graphs for the different regions for easier 
     comparison. analysis ignores null values.

    Args: 
        none.

    Returns:
        a graph of the change in income over time. plot saved as .png
    """   
    
    over_time = defaultdict(list) # dictionary of mean icome per person for region. keys are regions.
    
    for i in income.index:
        merged = merge_by_year(i)
        for region in countries.Region.unique():
            income_per_region = merged.Income[merged.Region== region].mean()
            over_time[region].append(income_per_region)
    
    DF = pd.DataFrame(over_time, index=income.index)
    
    plt.plot(DF.index,DF.values)
    plt.legend(DF.columns, loc = 2)
    plt.xlabel("Year")
    plt.ylabel("Income")
    plt.xlim((DF.index[0],DF.index[-1]))
    plt.title("Change of Income over time")
    plt.savefig("Change of Income over time in all regions")
    plt.show()
    return DF

def spreadByYear(year):
    """ Plots (boxplot) the spread of income per person for the regions for a given year.
    Args: 
        year: int. the year for which the distribution is calculated.

    Returns:
        a  box plot demostratint the difference in the spread of income per person for the different regions.
    """   
    merged = merge_by_year(year)
    spread = []
    for region in merged.Region.unique():
        spread_per_region = merged.Income[merged.Region== region]
        spread.append(spread_per_region.values)

    rcParams['figure.figsize'] = 15,7
    plt.boxplot(spread)
    ticks = list(merged.Region.unique())
    ticks.insert(0, "")
    plt.xticks(range(7), ticks, color='red')
    plt.ylabel("Income")
    plt.title("Spread of  of Income for the year %s" %year)
    plt.savefig("Spread of  of Income for the year %s" %year)
    plt.show()
   

if __name__ == "__main__":

    countries, income  = loadData()

    #Question 2: 
    print "Head of income DF: \n", income.head()

    #Question 3:
    incomeDistribution(2000)

    #Question 4:
    merged = merge_by_year(2000)
    print "Head of merged DF: \n", merged.head()

    #Quetion 5:
    incomeOverTime("Afghanistan")

    distributionOfIcomeByRegion(2010)

    MeanIncomeOverTime("AFRICA")

    DF = MeanIncomeOverTimeAllRegions()

    spreadByYear(2010)

    """ Analysis of the graphs has shown that aggragating all countries, the distribution of income is right skewed. We can also tell that while Europe boasts the highest income per person, the income has decreased in recent years. Europe is also the region that has the largest spread in income per person in recent years (this is easy to see through the boxplot).In addition,  we can see that in recent years Asia is experiencing the steepest ascent in income per person. """


