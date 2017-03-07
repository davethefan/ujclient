import bs4 as bs
import urllib.request
#locsearch = input ('Please enter location to search for jobs:')
# this does not work because cannot append string to url

sauce = urllib.request.urlopen("https://jobsearch.direct.gov.uk/JobSearch/PowerSearch.aspx?redirect=http%3A%2F%2Fjobsearch.direct.gov.uk%2Fhome.aspx&pp=25&pg=1&where=Sheffield%2C%20South%20Yorkshire%2C%20England&sort=rv.dt.di&rad=20&rad_units=miles&re=134").read()
soup = bs.BeautifulSoup(sauce,'lxml')

for mobiletd in soup.find_all("div", class_="mobileTd"):
	print(mobiletd.find_all,"<br>")
