import sys
import json

from bottle import route
from bottle import run
from bottle import static_file
from build_histogram import bucket_log

@route('/')
def main_page():
    return static_file('index.html', root='static')

@route('/:filename')
def server_static(filename):
    print filename
    return static_file(filename, root='static')

@route('/api/data')
def data():
	return json.dumps(bucket_log('midtowndoornail.log'))

port = sys.argv[1] if len(sys.argv) > 1 else 8080
run(host='0.0.0.0', port=port)
