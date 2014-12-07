import string

class CaseDAO(object):

	def __init__(self, database):
		self.db = database
		self.mycases = database.mycases
		
	def find_cases(self, tag):
		list = []
		if (tag == ""):
			for case in self.mycases.find():
				list.append({'_id':case['_id'], 'os':case['os'], 'date':case['date'], 'time':case['time'], 'tags':case['tags']})
		else:
			for case in self.mycases.find({"tags" : tag}):
				list.append({'_id':case['_id'], 'os':case['os'], 'date':case['date'], 'time':case['time'], 'tags':case['tags']})
				
		return list
		
	def find_items(self, id):
		list = []
		#for id in case_id:
		for item in self.db[id].find().distinct("Web Browser"):
			list.append({'case_id':id, 'web_browser':item, 'item_count':self.db[id].find(item["Web Browser":item]).count() })
		return list
	
	def graph_items(self, case_id):
		data = "blah"
		
		return data