# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#print("hello world")
import visa
try:
    rm=visa.ResourceManager('C:\\Program Files (x86)\\IVI Foundation\\VISA\\WinNT\\agvisa\\agbin\\visa32.dll')
    myinst = rm.open_resource("TCPIP0::130.216.177.66::inst0::INSTR")
    myinst.timeout = 5000
    
    myinst.write("*CLS")
    myinst.write("*IDN?")
    print (myinst.read())
    
    myinst.close()
    print("Close instrument Connection")
except Exception as err:
    print ('Exception" '+str(err.message))
finally:
    print ('complete')
    
