# Enter your code for "Name Cleaning" here.
import re
final = []
fin = [x.strip() for x in open('leaderboard.txt', 'r')]
out = []
for line in fin:
    name, score = line.split(",")
    name = name.lstrip('0123456789')
    name = re.sub(r'^[A-Z]+(?![a-z])', '', name)
    name = re.sub(r'\b[A-Z]+\b( |$)', '', name)
    name = re.sub(r'\b[a-z][a-zA-Z]*\b( |$)', '', name)
    name = name.strip()
    if not name:
        name = "Invalid Name"
    out.append((name, score))

scores = set([x[1] for x in out])

for score in scores:
    temp = [x for x in out if x[1] == score]
    temp.sort(key=lambda x: x[0])
    final.extend(temp)
final.sort(key=lambda x: float(x[1]), reverse=True)
for line in final:
    name, score = line
    print(name, score, sep=",")