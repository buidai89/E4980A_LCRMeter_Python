# -*- coding: utf-8 -*-
"""
Created on Mon Aug  26 10:47:40 2019

@author: dai bui
"""

#This is the code I use to open the meter (You will need to put in your own address):
import pandas as pd

FILE_PATH='RsLs.csv'
Lslist=[]
Rslist=[]
Frequencylist=[]

try:
    #Read sample data, to save to csv later on.
    colnames = ['UID','Frequencylist','Lslist', 'Rslist']
    data = pd.read_csv(FILE_PATH, names=colnames, skiprows =1) #read csv to a dataframe 'data', skip first row
    Frequencylist=data.Frequencylist.tolist()  #extract freq. to a list
    Lslist=data.Lslist.tolist() #extract Ls to a list
    Rslist=data.Rslist.tolist()

except Exception as err:
    print ('Exception" '+str(err.message))
finally:
    data.to_csv('out.csv')  #Save a frame of data tp *.csv
    print ('data save to out.csv')
