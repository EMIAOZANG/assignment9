import pandas as pd 
import matplotlib.pyplot as plt

countries = pd.read_csv('countries.csv')
income = pd.read_excel('income.xlsx')
    
def question1():
    return countries, income

incomeTrans = income.T
incomeTrans.columns = incomeTrans.ix[0]
incomeTrans = incomeTrans[1:]
    
def question2():
    print incomeTrans.head()
    return incomeTrans
    
def question3(): 
    incomeTrans.ix[2000].hist()
    plt.ylabel('Number of countries')
    plt.xlabel('Income per person')
    plt.title('Distribution of Income Per Person in 2000')
    plt.show()
    plt.savefig('hist_income_per_person.png')

def merge_by_year(year):
    country_income = pd.DataFrame(incomeTrans.ix[year])
    country_income['Country'] = list(country_income.index)
    country_region_income = countries.merge(country_income, on = 'Country')
    country_region_income.columns = ['Country', 'Region', 'Income']
    return country_region_income

def plot_hist_region(df):
    df.hist('Income', by = 'Region')
    plt.xlabel('Income per person')
    plt.ylabel('Number of countries')
    plt.savefig('histogram_region.png')
    
def plot_box_region(df):
    df.boxplot('Income', by = 'Region')
    plt.ylabel('Income per person')
    plt.savefig('boxplots_region.png')

def main():
    print '-----------this is question 1-----------'
    print 'loading dataframes'
    question1()
    print '-----------this is question 2-----------'
    print 'showing the head of the dataset' 
    question2()
    print '-----------this is question 3-----------'
    print 'displaying histogram'
    question3()
    print '-----------this is question 4-----------'
    print 'showing merged dataframe with three columns'
    year = raw_input('please input a year')
    df = merge_by_year(int(year))
    print df
    print '-----------this is question 5-----------'
    print 'displaying histogram and box plots with regions'
    plot_hist_region(df)
    plot_box_region(df)

if __name__ == '__main__':
    main()
