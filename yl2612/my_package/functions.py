import pandas as pd
import matplotlib.pyplot as plt

def countries_income_hist(df, year):
    '''
    Display the distribution of income per person across all countries in the world 
    for any given year using histogram.
    '''
    year_income = df.ix[year].dropna()
    
    #show income in histogram and save the picture
    plt.figure()
    year_income.hist(bins=60)
    plt.ylabel('Number of countries')
    plt.xlabel('Income per person')
    plt.title('Income per person in Year {}'.format(year))
    plt.savefig('Income_per_person_in_Year_{}.png'.format(year))
    
    
def merge_by_year(year):
    '''
    merge the countries and income data sets for any given year.
    return a data frame with 3 columns titled 'Country', 'Region', 'Income'.
    '''
    countries = pd.read_csv('countries.csv')
    income = pd.read_csv('indicator gapminder gdp_per_capita_ppp.csv')
    rename_income = income.rename(columns = {'gdp pc test':'Country'}) #rename the 'gdp pc test' column to 'Country' in the 'income' data frame
    selected_income = rename_income[['Country',year]] #create a data frame with columns of the countries and the selected year
    rename_selected_income = selected_income.rename(columns = {year:'Income'}) #rename the year column to income in the 'selected_income' data frame
    merge_df = pd.merge(countries, rename_selected_income) #merge the countries and income data sets for the given year
    return merge_df

def Q5_hist(df):
    plt.figure()
    df.hist('Income', by=df['Region'], xlabelsize = 8, ylabelsize = 8)    
    
    
def Q5_boxplot(df):
    plt.figure()
    df.boxplot('Income', by = 'Region')


