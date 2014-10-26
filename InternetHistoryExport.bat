#Run this file as Admin
#Run this file in the same directory as DisplayHistory.ps1
#This batch script generates a .csv file (soon to be changed to just run the script and not generate the csv file)
#That .csv file is will be in the C drive.
#the final version of this batch will be to just run the ps1 file. the ps1 will do the exporting to a dbf file.
Powershell.exe -ExecutionPolicy Bypass -Command .\DisplayHistory.ps1 > C:\test2.csv

