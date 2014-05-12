def interleavings(a, b):
    perms = []
    # speed up the recursion
    lenA, lenB = len(a), len(b)
    lenAB = lenA + lenB

    def helper(word, ai, bi):
        if len(word) == lenAB:
            perms.append(word)
            return

        # get next letter available
        if (ai + 1) != lenA:
            helper(word + a[ai + 1], ai + 1, bi)

        if (bi + 1) != lenB:
            helper(word + b[bi + 1], ai, bi + 1)

    if a:
        helper(a[0], 0, -1)
    if b:
        helper(b[0], -1, 0)

    if not perms:
        perms = ['']

    return sorted(perms)