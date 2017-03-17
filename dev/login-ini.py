from ConfigParser import SafeConfigParser
from os.path import dirname, join, expanduser

INSTALL_DIR = dirname (__file__)

config = SafeConfigParser()
config.read([
	join(INSTALL_DIR, 'config.ini'),
	#expanduser('~/.ujclient.ini'),
	'config.ini'
	])

usingurl = config.get('server','url')
print 'Using URL: ', usingurl
