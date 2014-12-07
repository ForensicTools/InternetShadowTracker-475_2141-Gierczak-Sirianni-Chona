#from urlparse import urlparse
#from urllib.parse import urlparse
import urllib
import socket

class GraphUrl():
	QUERY_STRING = "http://api.hostip.info/get_json.php?position=true&ip="
	
	def convertUrl(self, urlList):
		domainAttr = {}
		ipAddr = ""
		responseJson = ""
		response = {}
		data = []
		
		for (var i = 0, n = urlList.length; i < n; i++):
			domainAttr = urlparse(urlList[i])	#Get domain name
			ipAddr = socket.gethostbyname( domainAttr.netloc )	#Lookup IP
			responseJson = urllib.urlopen(QUERY_STRING + ipAddr).read()	#Geoloc request
			response = json.load( responseJson )	#Parse JSON response
			
			contains = False
			for (var l = 0, m = data.length; l < m; l++):
				if ( data[l]["domain"] == domainAttr.netloc ):
					data[l]["hits"] += 1
					contains = True
					break
				
			if  contains == False:
				data.append({'domain':domainAttr.netloc, 'lat': response["lat"], 'lng':response["lng"], 'hits': 1})
			
		return data