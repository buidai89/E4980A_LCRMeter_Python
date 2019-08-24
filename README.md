# E4980A_LCRMeter_Python
 Python scipt to run frequency sweep
This is very basic python code and setup guideline to connect with Agilent E4980A LCR Meter.
I am using eithernet but similar approach can be done with USB connection.
The code is to automate sweeping frequency from 20Hz to 2MHz or whatever range you define and read inductance Ls and resitance Rs
The data is saved to a *.csv file int the same directory and the results will be plotted.

Requirement libraries:
Pandas: to work with csv files
pyVisa: to communicate with the instrument
pymeasure
