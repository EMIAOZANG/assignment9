'''
Created on 2014.11.16

@author: apple
'''

#transform the data set to have years as the rows and countries as the columns
#print the head of new dataframe
def transform_df(df):
    print 'Question2:'
    newdf = df.T
    print newdf.head()
    print '-------------------'
    return newdf

