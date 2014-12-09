InternetShadowTracker-475_2141-Gierczak-Sirianni-Chona
======================================================

#Introduction
This tool pulls browsing history data and visualizes it into : graphs showing how often someone visits a site graphs showing where the servers of the site are located.  shows location of where a website is hosted on a map.

<<<<<<< HEAD

test 10/22/2014 - AG

test 2 - 10/22 - 8:45pm

test 3 - 10/22 - 9:05pm

test 4 -10/23 - 4:52

Pull request #7 - sent to Prof Stackpole. - AG 10/26 

Pull Request #8 - sent to Prof. Stackpole - MXC 11/2

Pull Request #9 - sent  to Prof. Stackpole - MXC & AG 11/9
=======
##Dependencies
	* MongoDB
	* Python
	* pymongo
	* bottle

##Installation
###Tested on Windows 7 with Python 3.4.2

1. Install MongoDB
	> http://www.mongodb.org/

2. Install Python
	> https://www.python.org/

3. Install Python Modules
```bash
	# cd "Drive:\...\Python\Scripts\"
	pip install pymongo
	pip install bottle
```

4. Download GitHub Project
	> https://github.com/ForensicTools/InternetShadowTracker-475_2141-Gierczak-Sirianni-Chona

##Run Web Server
1. Start MongoDB Server
```bash
	# Create directory for database storage
	# cd "Drive:\...\MongoDB\bin\"
	mongod.exe --dbpath <dir>
```

2. Start Python Rest Interface
```bash
	# cd "Drive:\...\InternetShadowTracker\Web Interface\"
	py main.py
```

3. Open web browser
<<<<<<< HEAD
* localhost:8080
>>>>>>> fe4b27d42354f25cdaf4e49f833e9ba4fdd5280c
=======
	>localhost:8080

##Run Browsing History Extraction Scripts

•Step1: Download"BrowsingHistoryScripts" folder

•Step2: Go to the directory of this folder in command prompt

•Step3: The first script that needs to be run is thechosen1.bat. This batch script can be run by typing in .\thechosen1.bat
 
Alternatively you can double click the icon for the script and it should run.

•Step4: Once the .\thechosen1.bat has been run you will notice that there will be 2 CSV files. "mycases.csv" is the data you entered and stores vital data about the PC you extracted. It helps for later use when building a profile for the case. The other CSV is named after the caseID you entered in the command prompt. That contains the actual browsing history itself formatted to a CSV.

•Step5: The CSV must now be imported into a MongoDB database.
>>>>>>> 9a72797b59eb46960187f2025b9ee55a20f61e60
