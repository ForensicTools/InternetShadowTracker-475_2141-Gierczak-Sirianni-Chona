Reference: http://www.nirsoft.net/utils/browsing_history_view.html


Internet Explorer example:

C:\...\browsinghistoryview>BrowsingHistoryView.exe /LoadIE 1 /scomma "C:\index_dat_test1.txt" (or .csv)


						/LoadIE <0 | 1>
						/LoadFirefox <0 | 1>
						/LoadChrome <0 | 1>
						/LoadSafari <0 | 1>

*Specifies whether to load the history of IE/Firefox/Chrome/Safari Web browser. 0 = Don't load, 1 = Load.*




***********************************************************************************************************************************************



Adam's system IE9 path and command usage: 

Nirsoft - Browswing History View -This command worked with comma delimited values

C:\Users\US321217\Desktop\!!!CSEC_475_Win_Forensics_Stackpole\!!!Project_assignment\browser_extract_app\browsinghistoryview>BrowsingHistoryView.exe /LoadIE 1 /scomma "C:\index_dat_test1.txt"








old reference(don't use):


BrowsingHistoryView.exe /scomma \Users\US321217\AppData\Local\Microsoft\Windows\History\History.IE5\index.dat > index_2014_11_13.txt