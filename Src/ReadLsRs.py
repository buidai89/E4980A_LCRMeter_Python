# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 10:47:40 2018

@author: E6230
"""

#This is the code I use to open the meter (You will need to put in your own address):
import visa
#import pandas as pd
#import numpy as np
#import time

try:
    filename = 'data.csv'
    myfile = open(filename,'w')
    myfile.truncate() #delete file content
    
    rm=visa.ResourceManager('C:\\Program Files (x86)\\IVI Foundation\\VISA\\WinNT\\agvisa\\agbin\\visa32.dll')
    e4980a = rm.open_resource("TCPIP0::10.1.1.5::inst0::INSTR")
    e4980a.timeout = 10000
    
    e4980a.write("*CLS")
    e4980a.write("*IDN?")
    print (e4980a.read())

    # This is the code I use to change the meter to LSRS mode (you may need a different mode):
    e4980a.write(':VOLTage:LEVel 1')   # set the voltage level
    e4980a.write(':FREQuency:CW 1000000')   # set the voltage level    
    e4980a.write(':FUNCtion:IMPedance:TYPE LSRS')  # Page 313 of manual
    

    # This is the code I use to get the displayed impedance:
    e4980a.query(':FETCh:IMPedance:FORMatted?')
    e4980a.query(':FETCh:IMPedance:CORRected?')

    
    # Once I have the displayed impedance I split it into Ls and Rs
    inductanceAndResistance =  e4980a.query(':FETCh:IMPedance:FORMatted?')
    Ls = float(inductanceAndResistance.split(",")[0])
    Rs = float(inductanceAndResistance.split(",")[1])
    
    # I then store the numbers in a Pandas dataframe and write it out using #
    # <dataframename>.to_csv()
    # raw_data = {'Ls':[Ls, Ls, Ls],'Rs':[Rs, Rs, Rs]}
    # LsRsDataFrame = pd.DataFrame(raw_data,columns=['Ls','Rs'])
    # LsRsDataFrame.to_csv('example.csv')
    
    myfile.write(str(Ls)+' , ' + str(Rs) + '\n')
    myfile.close()
    # I would recommend using pandas for your CSV creation.
    
    e4980a.close()
    print("Close instrument Connection")
    

except Exception as err:

    print ('Exception" '+str(err.message))

finally:
    print ('complete')
