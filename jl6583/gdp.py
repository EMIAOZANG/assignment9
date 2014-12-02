'''
Created on Nov 13, 2014

@author: luchristopher
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import os
import superio



class PerCapitaGDP():
    '''
    A visualizer of the dataset
    '''


    def __init__(self, arg_income, arg_countries):
        '''
        Constructor
        '''
        self.__gdp_by_year = arg_income
        self.__countries_regions = arg_countries
        
                
    def __queryByYear(self,year):
        return self.__gdp_by_year.ix[year,:]     
    
    
    def plotIncomeHistByYear(self,year):
        '''
        generate a histogram of income in year
        '''
        record = self.__queryByYear(year)
#         plt.figure(figsize=(100,8))
#         plt.xticks
#         plt.axes(frameon=False)
        #use latex for better performance
        os.environ['PATH'] = os.environ['PATH'] + ':/usr/texbin'
        fig = plt.figure()
        plt.style.use('ggplot')
        record.hist(bins=100,alpha=0.5,edgecolor='none',linewidth=0,color='g',grid=False)
        plt.rc('text',usetex=True)
        plt.rc('font',family='sans_serif')
        plt.xlabel('Income per person')
        plt.ylabel('Number of countries')
        plt.title('Worldwide Distribution Of Income Per Person in {}'.format(year))
        plt.show()
        #ask if user wants to export the graph to a file
        superio.ifSaveFigure(fig,'Figures/distribution_of_income_histogram_{}'.format(year),'png')
        
        
    def plotIncomeBoxByYear(self,year):
        '''
        generate a boxplot of income in year
        '''
        record = self.__queryByYear(year)
        os.environ['PATH'] = os.environ['PATH'] + ':/usr/texbin'
        fig = plt.figure()
        plt.style.use('ggplot')
        plt.rc('text',usetex=True)
        plt.rc('font',family='Helvetica')
        plt.xlabel('Year')
        plt.ylabel('Income')
        plt.title('Worldwide Distribution Of Income Per Person in {}'.format(year))
        record.plot(kind='box')
        plt.show()
        superio.ifSaveFigure(fig,'Figures/distribution_of_income_boxplot_{}'.format(year),'png')

    def mergeByYear(self,years):
        '''
        merge the income and region data on an specific year
        '''
        gdp_1year = pd.DataFrame(self.__gdp_by_year.transpose()[years])
        merged_dataframe = self.__countries_regions.join(gdp_1year,on='Country')
        if type(years) == int:
            merged_dataframe.columns = ['Country', 'Region', 'Income']
        return merged_dataframe
    
    def mergeByYears(self,years):
        '''
        multi_year version for mergeByYear
        '''
        current_dataframe = pd.DataFrame()
        for year in years:
            temp_dataframe = self.mergeByYear(year)
            temp_dataframe.index=[year for x in range(temp_dataframe.shape[0])]
            current_dataframe = pd.concat([current_dataframe,temp_dataframe])
            print current_dataframe
        return current_dataframe
    
    def describeBy(self,key,years):
        '''
        Describing the income data in following ways:
        Histogram:
            the Histogram is used to demonstrate the annual change of income, a boxplot will be created for each continent within the years that has been specified by 'years'
        Boxplot:
            the Boxplot reveals the distribution of income within each continent, the function will create a figure including years Boxplot representing each
            year given in 'years'
        '''
#         fig, axes = plt.subplots(len(years),1) 
        record = self.mergeByYear(years)
        #generating boxplot
        plt.style.use('ggplot')
        axes_boxplot = record.boxplot(by='Region',figsize=(18,15))
#         for i in range(axes_boxplot.shape[0]):
#             for j in range(axes_boxplot.shape[1]):
#                 if j < axes_boxplot.shape[0]*axes_boxplot.shape[1]:
#                     axes_boxplot[i,j].set_xticklabels(['AFRICA','ASIA','EUROPE','NORTH AMERICA','SOUTH AMERICA','OCEANIA'].sort())
        fig_boxplot = plt.gcf()
        fig_boxplot.suptitle('The Distribution of Income Within Each Continent')
        plt.show()
        superio.ifSaveFigure(fig_boxplot,'Figures/distribution_of_income_boxplot_{}_{}'.format(years[0],years[-1]),'png')
        #generating histogram
        axes_hist = record.hist(alpha=0.5, edgecolor='none',linewidth=0,grid=False,by='Region',figsize=(12,12),legend=True)
        fig_hist = plt.gcf()
        fig_hist.suptitle('The Distribution of Income {}'.format(years))
        plt.show()
        superio.ifSaveFigure(fig_hist,'Figures/distribution_of_income_histogram_{}_{}'.format(years[0],years[-1]),'png')
            
            
            
            
        
