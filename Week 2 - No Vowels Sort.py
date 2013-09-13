def novowelsort(l):
    return sorted(l, key=lambda x: x.translate(str.maketrans('', '', 'aeiouAEIOU')))