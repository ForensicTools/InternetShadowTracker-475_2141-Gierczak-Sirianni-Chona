:This batch files needs to be in the same directory as "BrowsingHistoryView.exe" and "project_profile_column_order_3.cfg"
:This scripts asks the user for input then runs BrowsingHistoryView.exe, it then adds a custom config file that needs to be ... 
: ...in the same directory and then creates two CSV's. One CSV is the raw browsing data and is named after the case ID that was entered ny the user...
: ...the other CSV is named mycases.csv and contains case(s) information (like tags, OS, etc.)

@echo off
If NOT exist "%cd%mycases.csv" (
	echo _id,os,date,time,tags > ./mycases.csv
)

set /p id="Enter case ID: "
set /p systemOS="Enter OS: "
set /p tag="Enter a tag: "

echo %id%,%systemOS%,%date%,%TIME%,%tag% >> ./mycases.csv

%cd%\BrowsingHistoryView.exe /cfg %cd%\project_profile_column_order_3.cfg /scomma "%cd%\%id%.csv" /sort "3"
