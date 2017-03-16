import requests

payload = {
	'username': 'username',
	'password': 'password'
}

with requests.Session() as c:
	c.post('https://authenticate.gateway.gov.uk/sidp/SignIn.ashx?gwv=1.0&gwrealm=urn%3aTransformingLabourMarketServices&gwtheme=directgov&gwcategory=Ind', data=payload)
	r = c.get('https://jobsearch.direct.gov.uk/Home.aspx')
	
	print ('Login successful?')
	print 'Logout' in r.content 
	