import csv
import subprocess
import os

IMPORT_DIR = ".\\Import\\"
IMPORT_ARGS = "--type csv --headerline --db scans --file "
IMPORT_EXE = "mongoimport.exe "
MONGO_DIR = "\\Program Files\\MongoDB 2.6 Standard\\bin\\"

#Return list of files in the directory
def get_files():
	list = []
	for file in os.listdir(IMPORT_DIR):
		if os.path.isfile(os.path.join(IMPORT_DIR, file)):
			list.append(file)
	return list

#Imports files using mongoimport.exe in the bin directory
def import_files():
	list = get_files()
	if list:
		for file in list:
			subprocess.call(MONGO_DIR + IMPORT_EXE + IMPORT_ARGS + IMPORT_DIR + file)
			os.remove(IMPORT_DIR + file)