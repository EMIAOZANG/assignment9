import pandas as pd
import matplotlib.pyplot as plt

# question 1 
countries = pd.read_csv('countries.csv')
income = pd.read_excel('income.xlsx')

# question 2
# transpose the income DataFrame
income_trans = income.T 
income_trans.columns = income_trans.ix[0]
income_trans = income_trans[1:]
def question2():
    print income_trans.head()


def question3():
    income_trans.ix[2000].hist(bins = 30)
    plt.ylabel('Number of Countries')
    plt.xlabel('Income per Person')
    plt.title('Distribution of income per person in 2000')
    plt.savefig('histogram of distribution of income ')
    plt.show()

def merge_by_year(year):
    '''This function merges the countries and income data sets for 
    any given year'''
    country_income = pd.DataFrame(income_trans.ix[year])
    country_income['Country'] = list(country_income.index)
    country_region_income = pd.merge(countries, country_income, on ='Country')
    country_region_income.columns = ['Country', 'Region', 'Income']
    return country_region_income

def plot_hist_region(year):
    dataframe = merge_by_year(year)   
    dataframe.hist('Income', by='Region', xrot= 100, xlabelsize = 10, ylabelsize = 10, bins = 25, figsize = [10,10]) 
    plt.ylabel('Income per Person')
    plt.savefig('histogram_region.png')

def plot_box_region(year):
    dataframe = merge_by_year(year)
    dataframe.boxplot('Income',by = 'Region')
    plt.ylabel('Income per Person')
    plt.savefig('boxplot.png')


def main():

    print '---------------This is question 2----------------'
    print '-----------Dispay the head of the dataset--------'
    question2()
    print '--------------This is question 3---------------'
    print '---------------Show the histogram --------------'
    question3()
    print '--------------This is question 4---------------'
    print '--------------Show merged dataframe-------------'
    year = raw_input('Please input a valid year between 1800 and 2012')
    year = int(year)
    print merge_by_year(year)
    print '--------------This is question 5---------------'
    print '--------------Display histogram with regions--------'
    plot_hist_region(year)
    print '\n--------------Display boxplot with regions--------'
    plot_box_region(year)
    
if __name__ =='__main__':
    main()
    
    


