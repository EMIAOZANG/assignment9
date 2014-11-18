import pandas as pd

def loadExcel_df(xlsx):
    """load the excel file into pandas DataFrame with years as rows 
    and countries as columns. print  the head of this data set, and return dataFrame
    """
    excel_df=pd.read_excel(xlsx,'Data',index_col=0)
    #load the excel file into panda dataframe,and have the first column as index 
    return excel_df#return the income for future use


def loadCsv(csv):
    """load the csv file, print out the head of data set, return pandas DataFrame
    """
    csv_df=pd.read_csv(csv)
    #print csv_df.head() 
    return csv_df

def TransferDf(dataframe):
    """transfer the the dataframe to it's transpose
    print  head of new dataframe, and return a new dataframe
    """
    newdf=dataframe.T
    print newdf.head()
    return newdf


    