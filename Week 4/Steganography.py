fin = open('ncss-modified.bmp', 'rb')
fin.seek(10)
length = fin.read(4)
length = int.from_bytes(length, byteorder='little')
fin.seek(0)
fin.seek(length)
lsbs = []
for x in fin.read():
    lsbs.append(x & 1)

message = ""
for x in range(1, int(len(lsbs) / 8 + 1)):

    bits = lsbs[(x - 1) * 8:x * 8]

    num = 0
    for bit in bits[::-1]:
        num = (num << 1) | bit
    #num = int(''.join(list(map(str, bits))[::-1]), 2)
    if chr(num) == "\x00":
        break
    message += chr(num)

print(message)


