**This is a frequency sweep application for use with Rohde & Schwarz FSW spectrum analyzer and Rohde & Schwarz SMW signal generator. **

Intended use: Characterize a DUT across a range of frequencies with an automated sweep tool that can run natively on an FSW.

Video instructions and demonstration: https://rohdeschwarz-my.sharepoint.com/:v:/r/personal/luke_grantham_rsa_rohde-schwarz_com/Documents/Customer%20Files/Frequency_Sweep/Frequency_Sweep_Tutorial.mp4?csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=iFdioY


Instructions for use:
1.  Download the dist folder in this repository. This contains the executables that can be run on the FSW or a third PC that is LAN conected to the instruments. 
2.	Move the Frequency_Response.exe and Frequency_Response_Offset.exe files into C:\R_S\instr\ApplicationStarter\UserApplications on the FSW. This can be done by our instrument web control tool. 
3.	Set up your sweep parameters on the FSW:
  a.	Frequency Start: Freq hard key -> Start soft key 
  b.	Frequency Stop: Freq hard key -> Stop soft key
  c.	Sweep Points: Sweep hard key -> Sweep Config soft key -> Sweep Points
  d.	Reference Level: Ampt hard key -> Ref Level soft key
4.	Specify your SMW IP Address.
  a.	SCPI recorder button on the top toolbar of the screen, and then Settings tab and enter the IP address into the “IP Address or Computer Name of Signal Generator” 
      We are not using SCPI recorder for this, but it an easy place to specify your signal generator location so the application can pull that address.
5.	Set up the sweep level on the SMW:
  a.	Enter the value of your signal level for the sweep on the signal generator: Level hard key -> enter the level value.
6.	Add the applications to the FSW Application Starter tool.
  a.	Under Application Starter on the top toolbar of the screen, go to the User Applications tab. 
  b.	Press the “Add Application” button and navigate to C:\R_S\instr\ApplicationStarter\UserApplications on the FSW file explorer. Add each application to the tool. 
7.	When you are ready to take the sweep, press the application you want to run. 
  a.	If you want to take a simple sweep where the generator and analyzer are at the same frequency, run “Frequency Response” application.   
  b.	If you want to specify a generator offset, i.e. when you are using a frequency converting device, then run “Frequency Response Offset” application. 
8.	Results will be outputted in Trace 2. You can export by pressing the Trace hard key -> Trace Config soft key -> Trace/Data Ex/Import tab -> select trace to export and export to ASCII file. 
    


**For code editing: **
The code is contained in Frequency_Response_Offset.py that can be edited for custom functionality. It can be built using pyinstaller.

Created by:
Joe Faulkner: Joseph.Faulkner@rsa.rohde-schwarz.com, 
Bill Bock: Bill.Bock@rsa.rohde-schwarz.comm, 
Mark Lewis: Mark.Lewis@rsa.rohde-schwarz.com,
Luke Grantham, Luke.Grantham@rsa.rohde-schwarz.com


-------------------------TO DO----------------------------------
1. Add build flag for PC or on-instrument running
2. Add build flag for frequency offset Yes or No
