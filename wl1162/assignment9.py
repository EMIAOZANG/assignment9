from supplement import *

countries, income = load_data()

def merge_by_year(year):
    """merge a particular year data into the countries data set"""
    year_of_country=pd.DataFrame(income.loc[year])  # select the particular year that wants to merge
    merged=pd.merge(countries, year_of_country, left_on='Country', right_index=True, how='inner')  # merge the income of a given year to countries in countries data set and exclude missing values
    merged=merged.rename(columns={year: 'Income'})  # change the column name from year to Income
    return merged


def main():
    year=input('Enter a year from 1800 to see the income distribution: ')
    plot_income_distribution(income, year)  # Problem 3 plot
    for i in range(2000, 2012, 2):  # Problem 5 plots
        plot_region_hist(merge_by_year(i))
        plt.savefig('histogram of region income in %s' % i)
        plot_region_boxplot(merge_by_year(i))
        plt.savefig('boxplot of region income in %s' % i)
        print 'Plotting Figures for %s' % i

if __name__=='__main__':
	main()

# Problem 5 answers:
# The plots show that in rencent years, North American and European countries have slightly decrease in their income distribution
# while Asian and South American countries steadily have their increasing income distribution  