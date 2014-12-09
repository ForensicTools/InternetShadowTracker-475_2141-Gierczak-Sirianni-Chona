import string
from urllib.parse import urlparse
import urllib.request
import socket
import json

class CaseDAO(object):

	#Initialize constants
	def __init__(self, database):
		self.db = database
		self.mycases = database.mycases
		self.QUERY_STRING = "http://api.hostip.info/get_json.php?position=true&ip="
	
	#Return list of cases filtered by tag search
	def find_cases(self, tag):
		list = []
		if (tag == ""):
			for case in self.mycases.find():
				list.append({'_id':case['_id'], 'os':case['os'], 'date':case['date'], 'time':case['time'], 'tags':case['tags']})
		else:
			for case in self.mycases.find({"tags" : tag}):
				list.append({'_id':case['_id'], 'os':case['os'], 'date':case['date'], 'time':case['time'], 'tags':case['tags']})
				
		return list
	
	#Return list of browser history within selected cases
	def find_items(self, id):
		list = []
		#for id in case_id:
		for item in self.db[id].find().distinct("Web Browser"):
			list.append({ 'case_id':id, 'web_browser':item, 'item_count':self.db[id].find( {"Web Browser":item }).count() })
		return list
	
	#Return an array of value key pairs with domain, latitude, longitude, and count
	def graph_items(self, queries):
		list = []
		valuePairs = []
		
		#for query in queries:
		valuePairs = queries.split(":")
		for request in self.db[ (valuePairs[0]) ].find( {"Web Browser": valuePairs[1] } ):
			list.append(request['URL'])
		
		return self.convUrl(list)
		
	def convUrl(self, urlList):		
		domainAttr = {}
		response = {}
		jsonResponse = ""
		ipAddr = ""
		data = []
		
		for url in urlList:
			domainAttr = urlparse(url)	#Get domain name
			ipAddr = socket.gethostbyname( domainAttr.netloc )	#Lookup IP
			jsonResponse = urllib.request.urlopen(self.QUERY_STRING + ipAddr).read()	#Geoloc request
			response = json.loads( jsonResponse.decode('utf-8'))	#Parse JSON response
			
			if response['lat'] is not None: #Error checking
				contains = False
				for point in data:
					if ( point['domain'] == domainAttr.netloc ):
						point['hits'] += 1 #Increment if it exists
						contains = True
						break
					
				if  contains == False: #Create new entry if it does not exist
					data.append({'domain':domainAttr.netloc, 'lat': response['lat'], 'lng':response['lng'], 'hits': 1})
			
		return data