'''
Created on Dec 2, 2014

@author: luchristopher
'''
import re
from userexcps import InvalidInputError

def year_parser(year_str):
    '''
    check if the input year string is legal
    '''
    if re.match(re.compile(r'^s*(((18|19)\d\d)|((200\d)|(201[012])))\s*$'),year_str):
        secured_input = int(re.search(re.compile(r'^(((18|19)\d\d)|((200\d)|(201[012])))$'),year_str).group())
    else:
        raise InvalidInputError()
    return secured_input
        
def years_parser(years_str):
    '''
    Takes a string as the input sequence of years, the function will check if the string is in the form '   YYYY  ,  YYYY , YYYY ....'
    (YYYY represents valid years) and throws an exception if the input string is not in the correct format, the function will return 
    a list of integers (sorted in ascending order) representing a sequence of years.
    ''' 
    pattern = re.compile(r'^\s*(((18|19)\d\d)|((200\d)|(201[012])))(\s*,\s*(((18|19)\d\d)|((200\d)|(201[012]))))*\s*$')
    if re.match(pattern,years_str):
        secured_string_list = re.findall(re.compile(r'\d{4}'),years_str)
        secured_year_list = map(int,secured_string_list)
        secured_year_list.sort()
    else:
        raise InvalidInputError()
    return secured_year_list

        
        
                