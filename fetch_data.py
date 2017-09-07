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
        # with open("page.html", "r+") as f:
        #     f.write(page)
        # f = open("page.html", "r+")
        # return f
        return page

    def extract_conent(self, page):
        soup = BeautifulSoup(page, "html.parser")#only "html parser" works on my mac
        content = ''
        for i in soup.find_all('p'):
            content += soup.find_all('p')[i].text
        content = content.encode('ascii', 'ignore').decode('ascii')
        with open("content.txt", "r+") as f:
            f.write(content)