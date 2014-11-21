# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 13:22:46 2014

@author: LaiQX
"""

class year_out_of_range(Exception):
    '''
    raise when the input year is not in the range [1800,2012]
    '''
    pass

class not_a_valid_year(Exception):
    '''
    raise when the input year is not a vaild number
    '''
    pass

class invalid_plot_mode(Exception):
    '''
    raise when the user choose a undefined plot mode
    '''
    pass