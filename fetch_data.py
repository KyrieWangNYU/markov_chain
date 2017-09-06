import urllib2
from markov_python.cc_markov import MarkovChain
from bs4 import BeautifulSoup
import re
# url = raw_input("Enter the address you want to retrieve: ")
url = 'https://ebooks.adelaide.edu.au/c/chesterton/gk/c52fb/chapter1.html'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
page = response.read()

# with open("page.html", "r+") as f:
#     f.write(page)

# with open("page.txt") as fp:
#     soup = BeautifulSoup(fp)
# f = open("page.html", "r+")
soup = BeautifulSoup(page, "html.parser")#only "html parser" works on my mac
print type(soup)
print soup.text
# content = soup.find_all('p')
# # print content
#
# if len(content) > 0:
#     for i in content:
#         with open("content.txt", "r+") as f:
#             f.write(str(i))

