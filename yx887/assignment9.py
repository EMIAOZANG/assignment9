import pandas as pd
import sys
import matplotlib.pyplot as plt

# Question 4
def merge_by_year(income, countries, year):
    """ Merge income data of specified year with country data """
    new_df = countries.join(income[year], how='inner')
    new_df.reset_index(level=0, inplace=True)
    new_df.columns = ['Country', 'Region', 'Income']
    return new_df

def plot_stack_hist(new_df, year):
    regions = new_df['Region'].unique()
    data = []
    for region in regions:
        data.append(new_df[new_df['Region']==region].Income)
    cm = plt.get_cmap('Greys')
    colors = [cm(x) for x in [0.833, 0.667, 0.5, 0.333, 0.167, 1]]
    plt.figure()
    plt.hist(data, bins=20, color=colors, stacked=True, label=list(regions))
    plt.title('Stacked Distribution of Income per Person by Region in {}'.format(year))
    plt.legend()
    plt.savefig('dist_by_region_{}.png'.format(year))
        
def plot_box(new_df, year):
    plt.figure()
    new_df.boxplot('Income', by='Region')
    plt.title('Boxplot of Income per Person by Region in {}'.format(year))
    plt.ylabel('income per person $')
    plt.ylim(0, 100000)
    plt.savefig('box_by_region_{}.png'.format(year))
    
def main():
    # Question 1
    args = sys.argv[1:]
    try:
        income = pd.read_excel(args[0], index_col=0)
        countries = pd.read_csv(args[1], index_col=0)
    except:
        print 'Please specify gdp and countries files in order'
        sys.exit()

    # Question 2
    income_t = income.transpose()
    print 'income data loaded!'
    print income_t.head()

    # Question 3
    try:
        year = input('Choose a year you want to see the distribution of income: ')
    except (EOFError, KeyboardInterrupt):
        print 'Bye!'
        sys.exit()
    data = income[year]
    plt.figure()
    n, bins, _ = plt.hist(data.dropna(), bins=20, color='gray')
    plt.title('Distribution of income per person in {}'.format(year))
    plt.xlabel('income per person $')
    plt.text(0.6*data.max(), 0.7*n.max(), 'Max({0}): {1:.2f}\nMin({2}): {3:.2f}'.format(data.argmax(), data.max(), data.argmin(), data.min()))
    plt.show()

    # Question 5
    for y in range(2007, 2012):
        df = merge_by_year(income, countries, y)
        plot_stack_hist(df, y)
        plot_box(df, y)

    # We can see from the boxplots that from 2008, there is slight decrease in income in Europe/North America while Asia and South America have increasing trends.
    
if __name__ == '__main__':
    main()
