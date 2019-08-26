# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 10:47:40 2018

@author: dai bui
"""

#This is the code I use to open the meter (You will need to put in your own address):
import visa
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
    # Setup the LCR
    
    rm=visa.ResourceManager('C:\\Program Files (x86)\\IVI Foundation\\VISA\\WinNT\\agvisa\\agbin\\visa32.dll')
    e4980a = rm.open_resource("TCPIP0::130.216.177.66::inst0::INSTR")
    e4980a.timeout = 10000 
    e4980a.write("*CLS")
    e4980a.write("*IDN?")
    print (e4980a.read())

    e4980a.write(':VOLTage:LEVel 1')   # set the voltage level
    e4980a.write(':FREQuency:CW 1000000')   # set the frequency
    e4980a.write(':FUNCtion:IMPedance:TYPE LSRS')  # Page 313 of manual
    
    # setup list
    e4980a.write(':LIST:CLEar:ALL')     #Clear list
    e4980a.write(':LIST:FREQuency 100000,109500,119000,128500,138000,147500,157000,166500,176000,185500,195000,204500,214000,223500,233000,242500,252000,261500,271000,280500,290000,299500,309000,318500,328000,337500,347000,356500,366000,375500,385000,394500,404000,413500,423000,432500,442000,451500,461000,470500,480000,489500,499000,508500,518000,527500,537000,546500,556000,565500,575000,584500,594000,603500,613000,622500,632000,641500,651000,660500,670000,679500,689000,698500,708000,717500,727000,736500,746000,755500,765000,774500,784000,793500,803000,812500,822000,831500,841000,850500,860000,869500,879000,888500,898000,907500,917000,926500,936000,945500,955000,964500,974000,983500,993000,1002500,1012000,1021500,1031000,1040500,1050000,1059500,1069000,1078500,1088000,1097500,1107000,1116500,1126000,1135500,1145000,1154500,1164000,1173500,1183000,1192500,1202000,1211500,1221000,1230500,1240000,1249500,1259000,1268500,1278000,1287500,1297000,1306500,1316000,1325500,1335000,1344500,1354000,1363500,1373000,1382500,1392000,1401500,1411000,1420500,1430000,1439500,1449000,1458500,1468000,1477500,1487000,1496500,1506000,1515500,1525000,1534500,1544000,1553500,1563000,1572500,1582000,1591500,1601000,1610500,1620000,1629500,1639000,1648500,1658000,1667500,1677000,1686500,1696000,1705500,1715000,1724500,1734000,1743500,1753000,1762500,1772000,1781500,1791000,1800500,1810000,1819500,1829000,1838500,1848000,1857500,1867000,1876500,1886000,1895500,1905000,1914500,1924000,1933500,1943000,1952500,1962000,1971500,1981000,1990500,2000000')  # Page 313 of manual
    
    #Frequency Sweeping
    Frequency = FREQUENCY_LOW
    while ((Frequency >= FREQUENCY_LOW) and (Frequency <= FREQUENCY_HIGH)):
            e4980a.write(':FREQuency:CW ' + str(Frequency))   # set the frequency
            inductanceAndResistance =  e4980a.query(':FETCh:IMPedance:FORMatted?')
            Ls = float(inductanceAndResistance.split(",")[0])
            Rs = float(inductanceAndResistance.split(",")[1])
            Lslist.append(Ls*1000000)   #convert to uH
            Rslist.append(Rs)
            Frequencylist.append(Frequency/1000000) #convert to Mhz
            Frequency += FREQUENCY_STEP 
    #Export data to csv
    MeasureDataSet = list(zip(Frequencylist,Lslist,Rslist))
    df = pd.DataFrame(MeasureDataSet,columns=['Freq(MHz)','Ls(uH)','Rs(Ohm)'])
    df.to_csv(FILE_PATH)
    
    #Close connection
    e4980a.close()
    print("Close instrument Connection")
    
    #Plot data
    f1=plt.figure()
    plt.plot(Frequencylist,Lslist)
    plt.xlabel('Frequency(MHz)')
    plt.ylabel('Inductance(uH)')
    plt.ylim(0,15)
    plt.grid(True)
    f1.show()
    #plt.show()

    f2=plt.figure()
    plt.plot(Frequencylist,Rslist)
    plt.xlabel('Frequency(MHz)')
    plt.ylabel('Series Resistance(Ohm)')
    plt.grid(True)
    f2.show()

except Exception as err:
    print ('Exception" '+str(err.message))
finally:
    print ('complete')
