import urllib2
#import cookiejar
import urllib
import requests
import mechanize
from mechanize._opener import urlopen
from mechanize._form import ParseResponse

USERNAME = 'UniversalJobmatchUsername'
PASSWORD = 'YourPassword'
URL      = "http://authenticate.gateway.gov.uk/authenticate.aspx?gwv=1.0&amp;gwrealm=urn%3aTransformingLabourMarketServices&amp;gwtheme=directgov&amp;gwcategory=Ind"
URLtest = "http://google.co.uk"
headers = [
    ('Accept', 'text/javascript, text/html, application/xml, text/xml, */*'),
    ('Content-type', 'application/x-www-form-urlencoded; charset=UTF-8'),
    ('User-Agent', 'Mozilla 5.0'),
]

browser = mechanize.Browser()
browser.addheaders = headers 
response = browser.open(URLtest)
browser.select_form(nr = 0)
browser.form['ctl00_fixedContent_Username_uid_UIDSingleField'] = USERNAME
browser.form['ctl00_fixedContent_Username_pw'] = PASSWORD

print response.geturl()
print response.read()
response.close()
