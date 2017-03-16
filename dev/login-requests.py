import requests
with requests.Session() as c:
	url = "https://authenticate.gateway.gov.uk/sidp/SignIn.ashx?gwv=1.0&gwrealm=urn%3aTransformingLabourMarketServices&gwtheme=directgov&gwcategory=Ind"
	USERNAME = "username"
	PASSWORD = "password"
	c.get(url)
	csrftoken = c.cookies['csrftoken']
	logindata = dict(csrfmiddlewaretoken=csrftoken,username=USERNAME, password=PASSWORD, next="https://jobsearch.direct.gov.uk/Home.aspx")
	c.post(url,data=logindata,headers={'Referer':'https://authenticate.gateway.gov.uk/sidp/SignIn.ashx?gwv=1.0&gwrealm=urn%3aTransformingLabourMarketServices&gwtheme=directgov&gwcategory=Ind'})
	page=c.get('https://jobsearch.direct.gov.uk/Home.aspx')
	print (page.content)
