InternetShadowTracker-475_2141-Gierczak-Sirianni-Chona
======================================================

#Introduction
This tool pulls browsing history data and visualizes it into : graphs showing how often someone visits a site graphs showing where the servers of the site are located.  shows location of where a website is hosted on a map.

##Dependencies
* MongoDB
* Python
* pymongo
* bottle

##Installation
###Tested on Windows 7 with Python 3.4.2

Install MongoDB: http://www.mongodb.org/

Install Python: https://www.python.org/

Install Python Modules
```bash
# cd "Drive:\...\Python\Scripts\"
pip install pymongo
pip install bottle
```

Download GitHub Project:https://github.com/ForensicTools/InternetShadowTracker-475_2141-Gierczak-Sirianni-Chona

###Run Web Server
Start MongoDB Server
```bash
# cd "Drive:\...\MongoDB\bin\"
# Create directory for database storage
mongod.exe --dbpath <dir>
```

###Start Python Rest Interface
* Change MONGO_DIR constant variable to reflect your MongoDB install path
* A Google Maps API key has been provided on line 9 of Graph.html for temporary use.  If used for extensive scans, please consider replacing with your own.
```bash
# cd "Drive:\...\InternetShadowTracker\Web Interface\"
py main.py
```

##Using the tool
###Extract Browser History
1. Download "BrowsingHistoryScripts" folder

2. Go to the directory of this folder in command prompt

3. The first script that needs to be run is thechosen1.bat. This batch script can be run by typing in .\thechosen1.bat.  Alternatively you can double click the icon for the script and it should run.

4. Once the .\thechosen1.bat has been run you will notice that there will be 2 CSV files. "mycases.csv" is the data you entered and stores vital data about the PC you extracted. It helps for later use when building a profile for the case. The other CSV is named after the caseID you entered in the command prompt. That contains the actual browsing history itself formatted to a CSV.

5. The CSV must now be imported into a MongoDB database.

###Graphing the data
1. Place the two CSV files generated previously into the "import" folder.  This can be found at the root of the project folder extracted from the zip.
  * There is testing data in this folder for to ensure the tool works
  
2. Open web browser: localhost:8080
  * This will import the two files into the database and delete them
  * If this fails you can manually import into the database by going to the mongoDB install path and executing "mongoimport.exe --type csv --headerline --db scans --file <File Name>
  
3. Case selection page
  * Search database by tags
  * Select desired case by clicking on item
  * Select all or none out of currently displayed page items
  * View selected case(s)
  
4. Browser history list
  * Search database by browser version
  * Select desired history by clicking on item
  * Select all or none out of currently displayed page items
  * Graph data
  
5. Viewing Graph data
  * Circles indicate amount of hits
  * Boxes display the domain of circle hit