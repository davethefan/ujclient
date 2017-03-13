import requests

url = 'http://authenticate.gateway.gov.uk/Authenticate.aspx?gwv=1.0&amp;gwrealm=urn%3aTransformingLabourMarketServices&amp;gwtheme=directgov&amp;gwcategory=Ind'
login_data = dict(ctl00_fixedContent_Username_uid_UIDSingleField='############', ctl00_fixedContent_Username_pw='password')
session = requests.session()
r = session.post(url, data=login_data)
r2 = session.get('https://jobsearch.direct.gov.uk/Home.aspx')
print (r2.content)


