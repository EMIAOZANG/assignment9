import pandas as pd
import matplotlib.pyplot as plt

#Loading two datasets.
print 'Loading countries.csv as countries'
countries = pd.read_csv('countries.csv')
print 'Loading indicator gapminder gdp_per_capita_ppp.xlsx as income.'
income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col='gdp pc test').T

def display(year):

	'''Display the distribution of income per person across all countries 
	in the world for any given year'''
	ax=income.loc[year,:].hist(bins=len(income.columns),alpha=0.3,normed=True)
	fig=ax.get_figure()
	fig.savefig('All_Country_in_{}.png'.format(year))

def merge_by_year(year):

    '''Merge the countries and income data sets for any given year.'''
    
    income_select=income.loc[year,:]
    income_select=pd.DataFrame(income_select)
    
    #Change the column name as 'Income', copy the index to a new 'Country' column
    income_select.columns=['Income']
    income_select['Country']=income_select.index
    
    #Merge two dataframe on 'Country'
    merge=countries.merge(income_select,on='Country',how='outer')
    
    return merge

def display_by_region(year):

	'''Use boxplots to explore the distribution of the income per person by region'''
	
	merge_select = merge_by_year(year)
	ax=merge_select.boxplot(by='Region',rot=90)
	fig=ax.get_figure()
	fig.savefig('boxplot_in_{}.png'.format(year))	
	plt.clf()
	
def display_change(start_year,end_year):

    '''Display the change in regions'''
    
    for i in range(start_year,end_year+1):
        if i==start_year:
            df_mean=merge_by_year(i).groupby(by='Region').mean()
            df_mean.columns=['income in {}'.format(i)]
        else:
            df_add = merge_by_year(i).groupby(by='Region').mean()
            df_mean['income in {}'.format(i)] = pd.Series(df_add['Income'])
	
    for i in range(len(df_mean)):
        plt.plot(range(start_year,end_year+1),df_mean.iloc[i,:],label='{}'.format(df_mean.index[i]))
   
	plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=3, fancybox=True, shadow=True)
	plt.savefig('change_from_{}_to_{}.png'.format(start_year,end_year))
