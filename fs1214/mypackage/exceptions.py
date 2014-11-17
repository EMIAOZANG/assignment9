'''
Created on 2014.11.15

@author: apple
'''

class YearInputException(Exception):
    def __str__(self):
        return "The input of year is not valid. It must be integer."
class YearBoundException(Exception):
    def __str__(self):
        return "The input of year is out of the bound. It must between 1800 and 2012."
