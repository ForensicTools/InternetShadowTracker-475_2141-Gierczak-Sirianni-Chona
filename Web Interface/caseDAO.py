import string

class CaseDAO(object):

	def __init__(self, database):
		self.db = database
		self.mycases = database.mycases
		
	def find_cases(self):
		l = []
		for each_case in self.mycases.find():
			l.append({'_id':each_case['_id'], 'os':each_case['os'], 'date':each_case['date'], 'time':each_case['time'], 'tags':each_case['tags']})
			
		return l