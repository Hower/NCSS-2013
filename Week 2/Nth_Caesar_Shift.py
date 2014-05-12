# Encodes a string by shifting each letter by n places.
# E.g., 'abc' shifted 2 places becomes 'cde'.
# Input the string then the number of places to shift
import string

alphaLen = 26
upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)

def caesar_shift(string, n):
    output = ""
    for char in string:
        if char.isalpha():
            if char.isupper():
                    output += upper[(n - (alphaLen - upper.index(char))) % alphaLen]
            else:
                    output += lower[(n - (alphaLen - lower.index(char))) % alphaLen]
        else:
            output += char
    return output

print(caesar_shift(input(), int(input())))