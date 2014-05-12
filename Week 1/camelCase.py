def to_camel(ident):
    for x in range(ident.count('_')):
        swap = ident.index('_') + 1
        ident = ident[0:swap] + ident[swap].upper() + ident[swap + 1:]
    return ident.replace('_', '')

print(to_camel(input()))