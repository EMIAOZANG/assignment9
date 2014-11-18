import pandas as pd
import dataLoading as dl 



def merge_by_year(year):
    """merge the countries and income dataset for any given year, 
    returns new Dataframe with three columns titles 'Country', 'Regions', 'Income'
    """
    income=dl.loadExcel_df('indicator gapminder gdp_per_capita_ppp.xlsx')
    countries=dl.loadCsv('countries.csv')
    merge = pd.merge(countries,income, how="inner",left_on='Country',right_index=True)
    #merge two dataframes by the name of countries
    merge=pd.concat([merge['Country'],merge['Region'],merge[float(year)]],axis=1)
    #create a new dataframes with a selected year to merge
    merge=merge.rename(columns = {year:'Income'})
    #rename the year columns as Income
    return merge
    
    
    
if __name__=='__main__':
    print merge_by_year(2000).head() # check the first 5 rows 
    
    