# -*- coding: utf-8 -*-
"""Assignment 9
   Mengfei Li
"""
from functions_assignment9 import *
import matplotlib.pyplot as plt



def main():
    
    
    countries,income,col,ind=data_input()
    print "---------------part 2----------------"
    print "The first 3 rows of modified income dataset: \n", income.head(n=3)
    
    
    print "---------------part 3----------------"
    year1=input('Year: ')
    plt.boxplot(income.ix[year1].dropna(),patch_artist=True)
    plt.title(str(year1))
    plt.show()

    
    print "---------------part 5----------------"
    
    
    year2=input('Input a year: ') 
    merged_df2=merge_by_year(year2)
    fig2,ax2=plt.subplots()
    ax2.hist(merged_df2.Income.dropna(),bins=50)
    plt.title(str(year2))
    plt.show()
    
    
    year3=input('Input the second one: ')
    merged_df3=merge_by_year(year3)
    fig3,ax3=plt.subplots()
    ax3.hist(merged_df3.Income.dropna(),bins=50,color='pink')
    plt.title(str(year3))
    plt.show()
    
    year4=input('Input another year: ')
    merged_df4=merge_by_year(year4)
    fig4,ax4=plt.subplots()
    ax4.hist(merged_df4.Income.dropna(),bins=50,color='purple')
    plt.title(str(year4))
    plt.show() 
    
    year5=input('Input a last year you want to display: ')
    merged_df5=merge_by_year(year5)
    fig5,ax5=plt.subplots()
    ax5.hist(merged_df5.Income.dropna(),bins=50,color='orange')
    plt.title(str(year5))
    plt.show() 
    
    
    #boxplots for recent 4 years 
    dat1=[merged_df2.Income,merged_df3.Income,merged_df4.Income,merged_df5.Income]    
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.boxplot(dat1,patch_artist=True)
    ax.set_xticklabels([year2,year3,year4,year5])
    
    #bar plot for each region's income average from 2009-2012
    dat2=pd.concat([merged_df2.groupby(['Region'])['Income'].mean(),merged_df3.groupby(['Region'])['Income'].mean(),merged_df4.groupby(['Region'])['Income'].mean(),merged_df5.groupby(['Region'])['Income'].mean()],axis=1)
    dat2.columns=[str(year2),str(year3),str(year4),str(year5)]
    dat2.plot(kind='bar')
            
if __name__=='__main__':
    main()