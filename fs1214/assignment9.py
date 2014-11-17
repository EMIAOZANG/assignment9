'''
Created on 2014.11.15

@author: apple
'''
from mypackage.question1 import *
from mypackage.question2 import *
from mypackage.question3 import *
from mypackage.question4 import *
from mypackage.question5 import *

        
def main():
    #Question1:
    countries,income = question1()
    
    #Question2:
    newincome = transform_df(income)
    
    #Question3:
    question3(newincome)
    
    #Question4:
    question4()
    
    #Question5:
    question5()
 
if __name__ == '__main__':
    main()