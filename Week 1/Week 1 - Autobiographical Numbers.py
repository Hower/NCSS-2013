def addDigits():
    total = 0
    for char in num:
        total += int(char)
    return total
def check():
    for pos, char in enumerate(num):
        if num.count(str(pos)) != int(char):
            return True
num = input("Number: ")
no = "is not autobiographical"
if len(num) != addDigits():
    print(num, no)
elif check():
    print(num, no)
else:
    print (num, "is autobiographical")
