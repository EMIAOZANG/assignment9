from basicfunctions import *


def main():
    '''
    Let the user test all the functions.
    '''
    print '-------------This is problem2-------------'
    dataframe = problem2()
    print
    print '-------------This is problem3-------------'
    print 'Please see attached picture showing the distribution of income per person across all countries in the world for year 2000'
    display(2000)
    print
    print '-------------This is problem4-------------'
    try:
        year = input('Input the year: ')
        print merge_by_year(year)
    except:
        print 'Something is wrong!'
    print
    print '-------------This is problem5-------------'
    print 'Please see the pictures generated showing the boxplots and histograms of year 2008-2012:'
    for year in range(2008, 2013, 1):
        boxplot(merge_by_year(year))
        plt.savefig('boxplot_{}.png'.format(year))
        histgram(merge_by_year(year))
        plt.savefig('histgram_{}.png'.format(year))



if __name__ == '__main__':
    main()
