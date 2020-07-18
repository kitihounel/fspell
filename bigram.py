from itertools import islice
from collections import Counter

def bigrams(w):
    """Returns a list containing the bigrams of a word."""
    s = "#" + w + "$"
    l = [x + y for x, y in zip(s, islice(s, 1, None))]
    return l

def similarity_score(v, w):
    """Computes the number of bigrams two words have in common."""
    c = Counter(bigrams(v))
    t = Counter(bigrams(w))
    return sum(min(c[k], t[k]) for k in c)
