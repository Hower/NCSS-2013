line = input("Line: ")
dic = []
while line:
    dic.append(line)
    line = input("Line: ")
for line in dic:
    output = ""
    for word in line.split():
        output += word[::-1] + " "
    print(output.rstrip())