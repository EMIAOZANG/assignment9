'''
Created on Nov 20, 2014

@author: keye
'''

class InvalidYearValue(Exception):
    """Raise when input is not a correct year value(integer)"""
    pass
        
class InvalidYearRange(Exception):
    """Raise when the input is not in the range of 1800 to 2012. """
    pass