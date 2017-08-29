import urllib2
from markov_python.cc_markov import MarkovChain
from bs4 import BeautifulSoup

# url = raw_input("Enter the address you want to retrieve: ")
url = 'http://www.google.com'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
page = response.read()

# with open("page.html", "r+") as f:
#     f.write(page)

# with open("page.html") as fp:
#     soup = BeautifulSoup(fp)

soup = BeautifulSoup(str(page),"html.parser")


print soup.prettify()