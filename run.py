from markov_python.cc_markov import MarkovChain
from fetch_data import *
welcome = "Welcome to markov_chain txt generater, you could choose " \
          "a website with novel or articles(e.g.online reader)"
print welcome
data = fetch_data()
url = raw_input("Enter the address you want to retrieve: ")
fname = data.generate_file(url)
data.extract_conent(fname)
mc = MarkovChain()
mc.add_file("content.txt")
length = raw_input("Enter the number of words you would like to generate: ")
con = []
while len(con) < int(length):
    con += mc.generate_text(20)
res = " ".join(con)
with open("result.txt", "r+") as f:
    f.writelines(res)
print "Result has been stored in result.txt"
# mc = MarkovChain()
# mc.add_file("content.txt")
# length = raw_input("Enter the number of word you would like to generate: ")
# con = []
# while len(con) < int(length):
#     con += mc.generate_text(20)
# res = " ".join(con)
# with open("res.txt", "r+") as f:
#     f.writelines(res)
