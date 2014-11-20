from package.exceptions import *
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pltpdf

#Check that the user input year is in a valid integer in range between 1800 and 2012 inclusive 
def isValidYear(year):
    try:
        year = int(year)
        if year >= 1800 and year <= 2012:
            return year
        else:
            raise notValidYearError('Not valid year')
    except:
        raise notValidYearError('Not valid year')

#Question 2.
def transform_dataset(income):   
    #transform income data set so rows are set to years and columns are set to countries
    transposed_ds = income.T
    #set columns to countries
    transposed_ds.columns = transposed_ds.ix[0]
    #remove first row
    final_income = transposed_ds.ix[1:]
    return final_income

#Question 3.
def graph_all_countries(trans_income, year):
    #Graph income per person across all countries in the world for given year
    #income_year is the row of income at given year with NAN's removed
    income_year = trans_income.ix[year]
    income_year = income_year.dropna()
    histogram = plt.figure()
    plt.hist(income_year,bins=50)
    plt.title('Histogram of Income Per Person Across All Countries in {}'.format(year))
    plt.xlabel('Income Per Person ($)')
    plt.ylabel('Number of Countries')
    histogram.savefig('Hist_Countries_{}'.format(year))
    
#Question 4.
def merge_by_year(countries, income, year):
    #merge countries and income data sets for any given year
    #result should be a dataframe with three columns: 'Country', 'Region', and 'Income'
    income = pd.DataFrame(income)
    #rename 'gdp pc test' column to 'Country'
    rename_income = income.rename(columns={'gdp pc test': 'Country'})
    #merge income and countries data on 'Country' column
    merged_df = rename_income[['Country', year]].merge(countries, on='Country')
    #rename column of incomes under given year to 'Income'
    merged_df = merged_df.rename(columns={year: 'Income'})
    #remove NaN's
    merged_df = merged_df.dropna()
    return merged_df

#Question 5.
#generate boxplots of Income Per Person for regions for each given year
def region_boxplot(merged_df, year):
    merged_df.boxplot('Income', by='Region')   
    plt.ylabel('Income per Person ($)')
    plt.savefig('Box_Regions_{}'.format(year))
    
#generate histograms of Income Per Person for regions for each given year
def region_histogram(merged_df, year):
    plt.figure()
    merged_df.hist('Income', by=merged_df['Region'], figsize=(20,10))
    plt.ylabel('Number of Countries')
    plt.xlabel('Income Per Person($)')
    plt.savefig('Hist_Regions_{}'.format(year))