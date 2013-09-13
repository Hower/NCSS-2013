import re
fin = open('sentences.txt', 'r').read().split("\n")
numOfLines = len(fin)
total = 0
mid = re.compile(r"[^A-Z][A-Z]{3}[^A-Z]")
start = re.compile(r"^[A-Z]{3}[^A-Z]")
only = re.compile(r"^[A-Z]{3}$")
end = re.compile(r"[^A-Z][A-Z]{3}$")
for line in fin:
    if mid.search(line) or start.search(line) or only.search(line) or end.search(line):
        total += 1
        print(line)
print("{:.1%} of sentences contain a TLA".format(total/numOfLines))