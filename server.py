import logging
import sys
import json

import bottle
from bottle import route
from bottle import run
from bottle import static_file

from vendor.scripts import build_histogram

bottle.debug(True)
log = logging.getLogger('servlet')
log.setLevel(logging.DEBUG)

@route('/')
def main_page():
    return static_file('index.html', root='static')

@route('/:filename')
def server_static(filename):
    print filename
    log.info(filename)
    return static_file(filename, root='static')

@route('/api/data')
def data():
    points = build_histogram.bucket_log('/home/derwiki/src/histogram/midtowndoornail-dates.log', format_output=True, bucket_seconds=300)
    data = dict((d, [count]) for d, count in points)
    print data.items()[0:10]
    print json.dumps(data)
    return json.dumps(data)

port = sys.argv[1] if len(sys.argv) > 1 else 8080
run(host='0.0.0.0', port=port)
