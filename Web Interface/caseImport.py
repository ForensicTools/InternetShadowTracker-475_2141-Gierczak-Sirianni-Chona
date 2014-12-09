import csv
import subprocess
from os import walk

class CaseImport(object):
	IMPORT_DIR = ".\\Import\\"
	IMPORT_ARGS = "--type csv --headerline --db mycases --file "
	IMPORT_EXE = "mongoimport.exe "
	MONGO_DIR = "\\Program Files\\MongoDB 2.6 Standard\\bin\\"
	
	#Return list of files in the directory
	def list_files(self):
		list = []
		for file in os.listdir(IMPORT_DIR):
			if os.path.isfile(os.path.join(IMPORT_DIR, file)):
				list.append(file)
		return list
	
	#Imports files using mongoimport.exe in the bin directory
	def import_files(self, list):
		NULL = open(os.devnull, 'w')
		for file in list:
			subprocess.call(MONGO_DIR + IMPORT_EXE + IMPORT_ARGS + IMPORT_DIR + file, stdout=NULL, stderr=NULL, shell=False)