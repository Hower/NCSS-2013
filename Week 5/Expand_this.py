class X:
    def __init__(self, pronumeral, exponent):
        self.pronumeral = pronumeral
        self.exponent = exponent

    def __str__(self):
        pronumeral = self.pronumeral
        exponent = '^' + str(self.exponent)
        if self.exponent == 1:
            exponent = ''
        if self.pronumeral < 0:
            pronumeral = -self.pronumeral
        if self.pronumeral == 1 or self.pronumeral == -1:
            pronumeral = ''
        return '{}x{}'.format(pronumeral, exponent)

    def __add__(self, other):
        # if they're both x and they have the same exponent
        if isinstance(other, X) and other.exponent == self.exponent:
            if self.pronumeral + other.pronumeral == 0:
                return 0
            return (X(self.pronumeral + other.pronumeral, self.exponent))

        else:
            return (self, other)

    def __mul__(self, other):
        # default assume "other" is an integer
        exponent = self.exponent
        # if it isn't, do the proper stuff
        if isinstance(other, X):
            exponent = self.exponent + other.exponent
            pronumeral = self.pronumeral * other.pronumeral
        else:
            pronumeral = self.pronumeral * other

        return (X(pronumeral, exponent))

    def __sub__(self, other):
        if isinstance(other, X) and other.exponent == self.exponent:
            if self.pronumeral - other.pronumeral == 0:
                return 0
            return (X(self.pronumeral - other.pronumeral, self.exponent))

        elif isinstance(other, X):
            return (self, X(-other.pronumeral, other.exponent))

        else:
            return (self, -other)


    def __pow__(self, exponent):
        if exponent == 0:
            return 1
        return (X(self.pronumeral**exponent, self.exponent * exponent))

def operate(a, b, c):
    # if the operand is a bracket term and we wan't to raise to a power
    if isinstance(a, tuple) or isinstance(c, tuple):
        if b in ['**', '*']:
            if b == '**':
                if c == 0:
                    return 1
                if c == 1:
                    return a
                # keep on multipying by itself up to the power
                result = a
                for x in range(1, c):
                    result = expand(result, a)
                return result
            else:
                return expand(a, c)
        else:
            toSimplify = []
            if not isinstance(a, tuple):
                a = [a]
            elif not isinstance(c, tuple):
                c = [c]
            # if it's minus, make all terms inside the
            # right bracket neg ative
            if b == '-':
                # gaah, wish I knew how to overload binary operators >.>
                c = [-term if not isinstance(term, X) else X(-term.pronumeral, term.exponent) for term in c]
            for x in a:
                toSimplify.append(x)
            for x in c:
                toSimplify.append(x)
            return simplify(toSimplify)
    # don't want to override int methods :/
    # if the first term is a int and the second term is x, return them
    # without modifying
    if isinstance(a, int) and isinstance(c, X) and b in ['+', '-']:
        if b == '-':
            return (a, X(-c.pronumeral, c.exponent))
        else:
            return (a, c)
    # if the operator is multiplication, reverse the operands
    if isinstance(a, int) and isinstance(c, X) and b == '*':
        return c * a
    return eval("a{}c".format(b))

# expand the brackets!
def expand(a, b):
    result = []
    if not isinstance(a, tuple):
        a = [a]
    if not isinstance(b, tuple):
        b = [b]
    for first in a:
        for second in b:
            if isinstance(first, int) and isinstance(second, X):
                result.append(second * first)
            else:
                result.append(first * second)

    return simplify(result)

def simplify(eq):
    result = []
    exponents = []
    # so we don't duplicate on the looping >.<
    unique = []
    exes = [term for term in eq if isinstance(term, X)]
    numbers = [term for term in eq if not isinstance(term, X)]
    for term in exes:
        if term.exponent not in exponents:
            exponents.append(term.exponent)
            unique.append(term)
    for term in unique:
        sameExponent = [x for x in exes if x.exponent == term.exponent and x is not term]
        simplified = term
        for x in sameExponent:
            simplified = simplified + x
        result.append(simplified)
    if numbers:
        total = 0
        for num in numbers:
            total += num
        result.append(total)
    return tuple(result)

operators = ['^', '+', '-', '*']
equation = input("RPN: ")
stack = []
for term in equation.split():
    if term not in operators:
        if term == 'x':
            term = X(1, 1)
        elif term == '-x':
            term = X(-1, 1)
        else:
            term = int(term)
        stack.append(term)
    else:
        if term == '^':
            term = '**'

        second = stack.pop()
        first = stack.pop()

        stack.append(operate(first, term, second))
def sorter(element):
    if isinstance(element, X):
        return element.exponent
    return -1
# sort

if len(stack) > 1:
    toSimplify = []
    for group in stack:
        if not isinstance(group, tuple):
            group = [group]
        for item in group:
            toSimplify.append(item)
    stack = [simplify(toSimplify)]

if isinstance(stack[0], tuple):
    stack = list(stack[0])

stack.sort(key=sorter, reverse=True)
out = ""
if stack == 0:
    print(0)
else:
    for index, item in enumerate(stack):
        if item == 0 and index != 0:
            continue
        if isinstance(item, X):
            if item.pronumeral < 0:
                if index != 0:
                    out += "- {} ".format(item)
                else:
                    out += "-{} ".format(item)
            elif index != 0:
                out += "+ {} ".format(item)
            else:
                out += "{} ".format(item)
        else:
            if item < 0:
                if index != 0:
                    out += "- {} ".format(-item)
                else:
                    out += "-{} ".format(-item)
            elif index != 0:
                out += "+ {} ".format(item)
            else:
                out += "{} ".format(item)
    print(out[:-1])
