import logging
import sys
import json

import bottle
from bottle import request
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
    log.info("Static: %s" % filename)
    return static_file(filename, root='static')

@route('/api/data')
def data():
    bucket_seconds = request.GET.get('bucket_seconds', 300)
    points = build_histogram.bucket_log('midtowndoornail-dates.log', format_output=True, bucket_seconds=bucket_seconds)
    data = dict((d, [count]) for d, count in points)
    return json.dumps(data)

port = sys.argv[1] if len(sys.argv) > 1 else 8080
run(host='0.0.0.0', port=port)
