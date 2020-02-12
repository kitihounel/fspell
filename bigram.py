from itertools import islice
from collections import Counter

def bigrams(w):
    """Return all the bigrams of a word"""
    s = "#" + w + "$"
    l = [a + b for a, b in zip(s, islice(s, 1, None))]
    return l

def similarity_score(w1, w2):
    """Compute the number of bigrams two words have in common"""
    c1 = Counter(bigrams(w1))
    c2 = Counter(bigrams(w2))
    return sum(min(c1[k], c2[k]) for k in c1)
