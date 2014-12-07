import bottle
import pymongo
import caseDAO
import caseImport

#Allow assets to be loaded (Images, css, etc.)
from bottle import static_file
@bottle.route('/assets/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./assets/')

#Web page: Index
@bottle.route('/')
def index_redir():
	return bottle.template('Index.html')

#Redirect to Index
@bottle.route('/Index.html')
def index():
	return bottle.redirect('/')

#Web page: List of cases currently in the database
@bottle.route('/CaseList.html')
def case_list():
	tag = bottle.request.query.tag
	mycase_list = case.find_cases(tag)
	return bottle.template('CaseList.html', dict(mycases = mycase_list))

#Web page: List of items within the selected case
@bottle.route('/Case.html')
def load_case():
	case_id = bottle.request.query.cases
	item_list = case.find_items(case_id)
	return bottle.template('Case.html', dict(myitems = item_list))

#Web page: Graphing the database
@bottle.route('/Graph.html')
def graph():
	return bottle.template('Graph.html')

#Server Connection
ServerAddr = "mongodb://localhost"
connection = pymongo.MongoClient(ServerAddr)
database = connection.scans
case = caseDAO.CaseDAO(database)

bottle.debug(True)
bottle.run(host='localhost', port=8080)