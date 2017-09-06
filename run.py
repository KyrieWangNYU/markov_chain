from markov_python.cc_markov import MarkovChain

mc = MarkovChain()
mc.add_file("content.txt")
# with open("content.txt") as f:
#     content = f.readlines()
# content = [x.strip() for x in content]
res = mc.generate_text(5)
with open("res.txt", "r+") as f:
    f.writelines(res)

