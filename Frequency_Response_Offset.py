## Frequency response program with SMW and FSW
## import modules
import pyvisa as py
import numpy as np
import time
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()  # Hide the main window



## Open resouces and assign to variables
rm = py.ResourceManager()

#Query the user for Frequency offset
Generator_Offset = int(float(simpledialog.askstring("Frequency Offset", "Please enter the generator frequency offset in MHz:"))*1000000)

#FSW_IP = simpledialog.askstring("Analyzer IP Address", "Please enter the FSW IP Address:") #COMMENT OUT FOR ON INSTRUMENT RUNNING
FSW_IP = "127.0.0.1"  #COMMENT OUR FOR PC RUNNING
#FSW_INST = rm.open_resource('TCPIP0::10.0.0.23::inst0::INSTR')
FSW_INST = rm.open_resource(f'TCPIP0::{FSW_IP}::inst0::INSTR')

#SMW_IP = simpledialog.askstring("Generator IP Address", "Please enter the SMW IP Address:")
SMW_IP = FSW_INST.query("CONF:GEN:IPC:ADDR?").replace("\n", "")
SMW_INST = rm.open_resource(f'TCPIP0::{SMW_IP}::inst0::INSTR')

## Ask user for inputs (Start/Stop Frequency, Sweep Points, Power Level)
#Start_Frequency= float(input("Please enter the start frequency in MHz: "))
Start_Frequency = FSW_INST.query_ascii_values("FREQ:STAR?")[0]
#Stop_Frequency= float(input("Please enter the Stop frequency in MHz: "))
Stop_Frequency = FSW_INST.query_ascii_values("FREQ:STOP?")[0]
#Sweep_Points = int(input("Please enter the number of sweep points to test: "))
Sweep_Points = FSW_INST.query_ascii_values("SWE:WIND:POIN?")[0]
#Power_Level = str(input("Please enter the generator power level in dBm: "))


## Build Frequency List
Frequency_List = np.linspace(Start_Frequency + Generator_Offset,Stop_Frequency + Generator_Offset,int(Sweep_Points))

#print(Frequency_List)

## Preset instruments
#SMW_INST.write("*RST")
#FSW_INST.write("*RST")
#time.sleep(1)

## Turn on RF, set reference level, set span, and change to peak detector
#SMW_INST.write("SOURce1:POWer:LEVel:IMMediate:AMPLitude "+Power_Level)
SMW_INST.write("OUTPut1:STATe 1")
#FSW_INST.write("DISP:WIND:TRAC:Y:SCAL:RLEV "+Power_Level)
#FSW_INST.write("SENS:FREQ:SPAN 100000000")
FSW_INST.write("SENS:FREQ:SPAN 20000000")
#FSW_INST.write("DISP:WIND1:SUBW:TRAC1:MODE MAXH")
FSW_INST.write("DISP:WIND1:SUBW:TRAC1:MODE WRIT")
FSW_INST.write("INIT:CONT OFF")
FSW_INST.write("FORM:DATA ASCII")
#time.sleep(.1)
## Empty list to store power readings
Power = []

## Iterate through frequency list, measure power, and store values in list
for i in range(len(Frequency_List)):
    #SMW_INST.write("SOURce1:FREQuency:CW "+str(Frequency_List[i-1])+"MHz")
    SMW_INST.write("SOURce1:FREQuency:CW "+str(Frequency_List[i]))
    #FSW_INST.write("SENS:FREQ:CENT "+str(Frequency_List[i-1])+"MHz")
    FSW_INST.write("SENS:FREQ:CENT "+str(Frequency_List[i] - Generator_Offset))
    #time.sleep(.05)
    FSW_INST.write("INIT:IMM;*WAI")
    #time.sleep(.05)
    #FSW_INST.write("CALC1:MARK1:STAT ON")
    FSW_INST.write("CALC1:MARK1:MAX:PEAK")
    Power_Value = FSW_INST.query_ascii_values("CALC1:MARK1:Y?")
    Power.append(Power_Value)

#print(len(Frequency_List))
#print(len(Power))
#print(Power)

#write trace2 with result
Power_Trace = (str(Power).replace("[", ""))
Power_Trace = Power_Trace.replace("]", "")

FSW_INST.write("TRAC:DATA TRACE2, " + str(Power_Trace))
FSW_INST.write("DISP:WIND1:SUBW:TRAC2:MODE VIEW")

FSW_INST.write("FREQ:STAR " + str(Start_Frequency))
FSW_INST.write("FREQ:STOP " + str(Stop_Frequency))
FSW_INST.write("SWE:WIND:POIN " + str(Sweep_Points))

FSW_INST.write("INIT:CONT ON")


