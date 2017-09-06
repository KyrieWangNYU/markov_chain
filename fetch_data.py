import urllib2
from markov_python.cc_markov import MarkovChain
from bs4 import BeautifulSoup

# url = raw_input("Enter the address you want to retrieve: ")
url = 'https://ebooks.adelaide.edu.au/c/chesterton/gk/c52fb/chapter1.html'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
page = response.read()

with open("page.html", "r+") as f:
    f.write(page)

# with open("page.txt") as fp:
#     soup = BeautifulSoup(fp)

soup = BeautifulSoup(str(page),"html.parser")
content = soup.find_all('p')
# print content
if len(content) > 0:
    for i in content:
        with open("content.txt", "r+") as f:
            f.writelines(str(i))

mc = MarkovChain()
mc.add_file("content.txt")
res = mc.generate_text(20)
with open("res.txt", "r+") as f:
    f.writelines(res)
# print soup.prettify()