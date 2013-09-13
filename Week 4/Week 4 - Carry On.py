def carries(a, b):
    count = 0
    carry = 0
    a, b = str(a), str(b)
    a = '0' * (len(b) - len(a)) + a
    b = '0' * (len(a) - len(b)) + b
    for x, y in zip(a[::-1], b[::-1]):
        x, y = int(x), int(y)
        d = x + y + carry
        if d >= 10:
            count += 1
            carry = int(str(d)[0])
        else:
            carry = 0
    return count
