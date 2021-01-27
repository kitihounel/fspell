from itertools import islice
from collections import Counter

def bigrams(w):
    """Returns a list containing the bigrams of a word."""
    s = "#" + w + "$"
    l = [x + y for x, y in zip(s, islice(s, 1, None))]
    return l

def similarity_score(v, w):
    """Computes Sorenson-Dice coefficient of two words."""
    vb = bigrams(v)
    wb = bigrams(w)
    vc = Counter(vb)
    wc = Counter(wb)
    return  2 * sum(min(vc[k], wc[k]) for k in wc) / (len(vb) + len(wb))
