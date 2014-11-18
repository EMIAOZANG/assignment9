import pandas as pd
import matplotlib.pyplot as plt

'''Question 1: pload the csv and excel file into pandas dataframes'''
countries = pd.read_csv('countries.csv')
income = pd.read_excel('Income_per_person.xlsx', index_col = 0)

'''Question 2: transform data set to have years a the rows and countries as the columns'''
income_T = income.T
def Question2():
  print income_T.head()

'''
Question 3: graphically display the distribution of income per person across all countries in the world for any given year.
I have chosen to display the distribution using a histogram because it best shows the frequency and range of distribution
'''

def Question3(year):
  income_T.loc[year,:].hist(bins=50)
  plt.ylabel('# of countries')
  plt.xlabel('Income per Person')
  plt.title('Distribution of Income per Person: 2000')
  plt.savefig('distribution of income in 2000 histogram')

  '''
  Question 4: the following codes merge the countries and income data sets for any given year'''
def merge_by_year(year):

  income_year = pd.DataFrame(income_T.ix[year]).reset_index()
  income_year.columns = ['Country','Income']
  income_year_region = pd.merge(income_year, countries,on='Country',how = 'inner')
  cols = ['Country','Region','Income']
  
  income_year_region = income_year_region[cols]

  return income_year_region

def main():
    
  '''questions 2'''
  print "the head of transformed income data \n"
  Question2()

  '''question 3'''
  Question3(2000)
  
  '''question 5'''
  for year in range(2002,2013):
    income_year = merge_by_year(year)
    income_year.boxplot('Income',by = 'Region',rot = 100,fontsize = 12,figsize = (15,15))
    plt.ylabel('income per person')
    plt.savefig('income_boxplot_%d.png' % (year))
    income_year.hist('Income',by='Region',xrot= 100, xlabelsize = 12, ylabelsize = 12,bins = 20,figsize = (15,15))
    plt.ylabel('income per person')
    plt.savefig('income_hist_%d.png' % (year))
    plt.close()

if __name__ == '__main__':
  main()



