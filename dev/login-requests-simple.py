import requests
import sys

payload = {
	'ctl00_fixedContent_Username_uid_UIDSingleField': 'username',
	'ctl00_fixedContent_Username_pw': 'password'
}

with requests.Session() as c:
	c.post('https://authenticate.gateway.gov.uk/sidp/SignIn.ashx?gwv=1.0&gwrealm=urn%3aTransformingLabourMarketServices&gwtheme=directgov&gwcategory=Ind', data=payload)
	r = c.get('https://jobsearch.direct.gov.uk/Home.aspx')
	
	#search for the word 'logout' in the body text, to return whether a user is logged in or not.
	print 'Logged in?:', 'Logout' in r.content