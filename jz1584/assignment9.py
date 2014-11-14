import dataLoading as dl
import merge
import matplotlib.pyplot as plt



def plotHist(dataFrame,year):
    """display the pandas DataFrame/Series in histogram """
    dataFrame.dropna()#drop the Nan value
    dataFrame.ix[float(year)].hist(bins=50)#display series  using histogram
    plt.ylabel('freq')
    plt.xlabel('(income/person interval in year of %s)'%year)
    plt.show()


def exploreData(tool,year):
    """ inputed tool is either  histogram or boxplot, then the function generates 
        histogram or boxplot to explore the distribution of the income per person 
        by region data set ,then show the corresponding figure
    """
    df=merge.merge_by_year(year)
    if tool=='boxplot':
        df.boxplot('Income',by='Region')
        plt.title('Year of %s'%year)
        plt.ylabel('Income / person')
        plt.show()       
    elif tool=='histogram':
        df.hist('Income',by=df['Region'])
        plt.xlabel(' Income interval in Year of %s'%year)
        plt.ylabel('freq')
        plt.show()



if __name__=='__main__':
    income=dl.loadExcel_df('indicator gapminder gdp_per_capita_ppp.xlsx')
    countries=dl.loadCsv('countries.csv')
    #answering question 1
    income=dl.TransferDf(income)
    #answering question 2
    plotHist(income,2000)
    #answering question 3
    merge.merge_by_year(2000)
    #answering question 4
    
    for year in range(2000,2010,1):#show the figure for each year in most recent 10 years
        exploreData('boxplot',year)
        #exploreData('histogram',year) # we could also try histogram
    #for example, explore the distribution of the income per person by region for the most recent 10 years
    #for Question5.
    # one of the most obvious change  we can could tell is ASIA region 
    #has the overall gdp per person increased a lot over past decade
        
    
    
    
 
