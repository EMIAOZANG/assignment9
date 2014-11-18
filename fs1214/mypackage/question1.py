'''
Created on 2014.11.16

@author: apple
'''
import pandas as pd

#load the countries.csv to dataframe
def load_csv(data_csv):
    df = pd.read_csv(data_csv)
    return df

#load the excel to dataframe
def load_excel(data_excel):
    df = pd.read_excel(data_excel,index_col=0)
    return df

def question1():
    countries = load_csv('countries.csv')
    income = load_excel('indicator gapminder gdp_per_capita_ppp.xlsx')
    return countries,income
