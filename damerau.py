def damerau_lev(seq1, seq2):
    """Calculates the Damerau-Levenshtein distance between two sequences.

    This distance is the number of additions, deletions, substitutions,
    and transpositions needed to transform the first sequence into the
    second. Although generally used with strings, any sequences of
    comparable objects will work.

    Transpositions are exchanges of *consecutive* characters; all other
    operations are self-explanatory.

    This implementation is O(N*M) time and O(M) space, for N and M the
    lengths of the two sequences.

    >>> dameraulevenshtein('ba', 'abc')
    2
    >>> dameraulevenshtein('fee', 'deed')
    2

    It works with arbitrary sequences too:
    >>> dameraulevenshtein('abcd', ['b', 'a', 'c', 'd', 'e'])
    2
    """
    # Conceptually, this is based on a len(seq1) + 1 * len(seq2) + 1 matrix.
    # However, only the current and two previous rows are needed at once,
    # so we only store those.
    oneago = []
    thisrow = list(range(1, len(seq2) + 1)) + [0]
    for i in range(len(seq1)):
        # Python lists wrap around for negative indices, so put the
        # leftmost column at the *end* of the list. This matches with
        # the zero-indexed strings and saves extra calculation.
        twoago, oneago, thisrow = oneago, thisrow, [0] * len(seq2) + [i + 1]
        for j in range(len(seq2)):
            delcost = oneago[j] + 1
            addcost = thisrow[j-1] + 1
            subcost = oneago[j-1] + (seq1[i] != seq2[j])
            thisrow[j] = min(delcost, addcost, subcost)
            # This block deals with transpositions
            if i > 0 and j > 0 and seq1[i] == seq2[j-1] and seq1[i-1] == seq2[j] and seq1[i] != seq2[j]:
                thisrow[j] = min(thisrow[j], twoago[j-2] + 1)
    return thisrow[len(seq2)-1]
