import collections
import datetime

# this is more correct but we can take a shortcut
#f = datetime.datetime.strptime
#events = (f(d.split(',')[1], '%Y-%m-%d %H:%M:%S-0700') for d in open('midtowndoornail.log')

# chopping off the string after 15 characters chops rounds to 10s of minutes
def bucket_log(logfile):
	events = (d.split(',')[1][:15] for d in open(logfile))
	buckets = collections.defaultdict(int)
	datetime_buckets = dict()
	for event in events: buckets[event] += 1

	f = datetime.datetime.strptime
	datetime_buckets = dict((f('%s0' % bucket, '%Y-%m-%d %H:%M'), count) for bucket, count in buckets.items())

	#for event_datetime, count in sorted(datetime_buckets.items()):
	#	print "[%s] %s" % (event_datetime, count)

	start_datetime = min(datetime_buckets.keys())
	datapoints = sorted(((event_datetime - start_datetime).seconds, count) for event_datetime, count in datetime_buckets.items())
	return datapoints
