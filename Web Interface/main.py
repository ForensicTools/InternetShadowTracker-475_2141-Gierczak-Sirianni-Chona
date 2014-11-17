import bottle
import pymongo
import caseDAO

#Set 
from bottle import static_file
@bottle.route('/assets/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./assets/')

@bottle.route('/')
def index_redir():
	return bottle.template('Index.html')

@bottle.route('/CaseList.html')
def case_list():
	mycase_list = case.find_cases()
	return bottle.template('CaseList.html', dict(mycases = mycase_list))

@bottle.route('/loadcase')
def load_case():
	case_id = bottle.request.query.id
	return bottle.redirect('Case.html?{{id}}', id=case_id)



#Server Connection
ServerAddr = "mongodb://localhost"
connection = pymongo.MongoClient(ServerAddr)
database = connection.scans
case = caseDAO.CaseDAO(database)

bottle.debug(True)
bottle.run(host='localhost', port=8080)