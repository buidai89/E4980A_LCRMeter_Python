# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 10:47:40 2018

@author: dai bui
readme: https://chrisalbon.com/python/data_wrangling/pandas_dataframe_importing_csv/
"""

#This is the code I use to open the meter (You will need to put in your own address):
import pandas as pd
import matplotlib.pyplot as plt


FREQUENCY_STEP = 10000
FREQUENCY_LOW = 10000
FREQUENCY_HIGH = 2000000
FILE_PATH='RsLs.csv'
Lslist=[]
Rslist=[]
Frequencylist=[]

try:
    colnames = ['UID','Frequencylist','Lslist', 'Rslist']
    data = pd.read_csv(FILE_PATH, names=colnames, skiprows =1)
    Frequencylist=data.Frequencylist.tolist()
    Lslist=data.Lslist.tolist()
    Rslist=data.Rslist.tolist()
    
    #Plot data
    
    plt.figure()
    plt.plot(Frequencylist,Lslist)
    plt.xlabel('Frequency(MHz)')
    plt.ylabel('Inductance(uH)')
    plt.ylim(0,15)
    plt.grid(color='grey', linestyle='--', linewidth=2)
    plt.show(block=True)

    plt.figure()
    plt.plot(Frequencylist,Rslist)
    plt.xlabel('Frequency(MHz)')
    plt.ylabel('Series Resistance(Ohm)')
    plt.grid(color='grey', linestyle='--', linewidth=2)
    plt.show(block=True)
    plt.show()

except Exception as err:
    print ('Exception" '+str(err.message))
finally:
    print ('complete')
