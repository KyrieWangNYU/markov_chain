import urllib2
from bs4 import BeautifulSoup

class fetch_data:


    # def get_url(self):
    #     url = raw_input("Enter the address you want to retrieve: ")
    #     # url = 'https://ebooks.adelaide.edu.au/c/chesterton/gk/c52fb/chapter1.html' This is an example
    #     return url

    def generate_file(self, url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        page = response.read()
        with open("page.html", "r+") as f:
            f.write(page)
        f = open("page.html", "r+")
        return f


    def extract_conent(self, f):
        soup = BeautifulSoup(f, "html.parser")#only "html parser" works on my mac
        content = []
        for i in soup.find_all('p'):
            content.append(i.text)
        content = "".join(content)
        content = content.encode('ascii', 'ignore').decode('ascii')
        with open("content.txt", "r+") as f:
            f.write(content)




# with open("page.txt") as fp:
#     soup = BeautifulSoup(fp)
# f = open("page.html", "r+")
# soup = BeautifulSoup(f, "html.parser")#only "html parser" works on my mac
# content = soup.find_all('p').text
# content = content.encode('ascii', 'ignore').decode('ascii')
# with open("content.txt", "r+") as f:
#     f.write(content)
# print type(soup)
#print soup.text
# content = soup.find_all('p')
# # print content
#

# content = soup.find_all('p')[0].text
# content = content.encode('ascii', 'ignore').decode('ascii')
# with open("content.txt", "r+") as f:
#     f.write(content)
