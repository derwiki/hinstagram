from bottle import route
from bottle import run
from bottle import static_file
from build_histogram import bucket_log

@route('/')
def main_page():
    return static_file('index.html', root='static')

@route('/:filename')
def server_static(filename):
    return static_file(filename, root='static')

@route('/api/data')
def data():
	return {'data': bucket_log('midtowndoornail.log')}

run(host='localhost', port=8080)