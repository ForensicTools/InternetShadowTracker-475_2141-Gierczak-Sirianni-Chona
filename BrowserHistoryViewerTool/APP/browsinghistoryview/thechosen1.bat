:This version creates a CSV without quotes
@echo off
If NOT exist "%cd%mycases.csv" (
	echo _id,os,date,time,tags > ./mycases.csv
)

set /p id="Enter case ID: "
set /p systemOS="Enter OS: "
set /p tag="Enter a tag: "

echo %id%,%systemOS%,%date%,%TIME%,%tag% >> ./mycases.csv

%cd%\BrowsingHistoryView.exe /cfg %cd%\project_profile_column_order_3.cfg /scomma "%cd%\%id%.csv" /sort "3"
