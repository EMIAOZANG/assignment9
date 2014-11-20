import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    """load two data into dataframe and display the header of transformed income data"""
    countries=pd.read_csv('countries.csv')  # load countries data set
    income=pd.read_excel('income.xlsx', sheetname=0, index_col='gdp pc test').T  # load income data set and transform it to have years as rows and countries as columns

    headers=income.columns.values.tolist()  # print the headers of income dataframe
    print headers
    return countries, income

def plot_income_distribution(dataframe, year):
    """plot the particular income distribution of a given year"""
    dataframe=pd.DataFrame(dataframe.loc[year])
    dataframe.hist(bins=100)
    plt.title('Year %s' % year)
    plt.xlabel('GDP/Capita')
    plt.ylabel('Countries count')
    plt.savefig('Income Distribution of %s' % year)

def plot_region_hist(dataframe):
    """plot the income histogram by region in a given year"""
    dataframe.hist('Income', by=dataframe['Region'], bins=50)
    

def plot_region_boxplot(dataframe):
    """plot the income boxplot by region in a given year"""
    dataframe.boxplot('Income', by='Region')
    

