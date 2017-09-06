from markov_python.cc_markov import MarkovChain

mc = MarkovChain()
mc.add_file("content.txt")
length = raw_input("Enter the number of word you would like to generate: ")
con = []
while len(con) < int(length):
    con += mc.generate_text(20)
res = " ".join(con)
with open("res.txt", "r+") as f:
    f.writelines(res)
