from string import punctuation
import math

out = []

# Read in comparison text
lengths = [len(word.strip(punctuation)) for word in open('unknown.txt', 'r').read().split()]
compare = [lengths.count(x) for x in range(1, max(lengths) + 1)]

for bookName in open('texts.txt', 'r'):

    bookName = bookName.strip()
    book = open(bookName, 'r').read()

    lengths = [len(word.strip(punctuation)) for word in book.split()]
    freq = [lengths.count(x) for x in range(1, max(lengths) + 1)]

    # Pad the ends of the lists so they're the same length
    compare.extend([0] * (len(freq) - len(compare)))
    freq.extend([0] * (len(compare) - len(freq)))

    numerator = 0
    ADenom = 0
    BDenom = 0

    # Apply equation and add to output buffer
    for a, b in zip(freq, compare):
        numerator += a * b
        ADenom += a**2
        BDenom += b**2
    denom = math.sqrt(ADenom) * math.sqrt(BDenom)
    sim = numerator/denom
    out.append((sim, bookName))

# Print in decending order
for line in sorted(out, key=lambda x: x[0], reverse=True):
    print("{:.3f} {}".format(line[0], line[1]))