output = ""
number = input("Number: ")
width = int(input("Width: "))

# Split into top, center and bottom segments
seg1, seg2, seg3 = 1, width + 2, width * 2 + 3

# Map numbers to segments they generate
dic = {}
dic[1] = [3, 6]
dic[2] = [1, 3, 4, 5, 7]
dic[3] = [1, 3, 4, 6, 7]
dic[4] = [2, 3, 4, 6]
dic[5] = [1, 2, 4, 6, 7]
dic[6] = [1, 2, 4, 5, 6, 7]
dic[7] = [1, 3, 6]
dic[8] = [1, 2, 3, 4, 5, 6, 7]
dic[9] = [1, 2, 3, 4, 6, 7]
dic[0] = [1, 2, 3, 5, 6, 7]

def check(lineNum, draw):
    line = ""
    if lineNum in [seg1, seg2, seg3]:
        if lineNum == seg1 and 1 in draw or \
        (lineNum == seg2 and 4 in draw) or \
        (lineNum == seg3 and 7 in draw):
            return " " + "-" * width + " "
        else:
            return " " * (width + 2)

    if lineNum < seg2 and 2 in draw or \
    (lineNum < seg3 and lineNum > seg2 and 5 in draw):
        line = "|" + " " * width
    else:
        line = " " * (width + 1)

    if lineNum < seg2 and 3 in draw or \
    (lineNum < seg3 and lineNum > seg2 and 6 in draw):
        line += "|"
    else:
        line += " "

    return line

for lineNum in range(1, 2 * width + 4):
    for digit in number:
        output += check(lineNum, dic[int(digit)]) + " "

    # Remove trailing whitespace
    print(output[:-1])
    output = ""