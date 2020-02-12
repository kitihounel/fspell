from collections import deque
from itertools import islice
from fspell_utils import strip_tones
from damerau import damerau_lev
from bigram import similarity_score

class _Node:
    def __init__(self, w):
        self.words = [w]
        self.key = strip_tones(w)
        self.children = {}

    def add_word(self, w):
        k = strip_tones(w)
        d = damerau_lev(self.key, k)
        if d == 0:
            self.words.append(w)
            return

        current = self
        child = current.children.get(d, None)
        while child is not None:
            current = child
            d = damerau_lev(current.key, k)
            if d == 0:
                current.words.append(w)
                return
            child = current.children.get(d, None)
        current.children[d] = _Node(w)

    def words_with_similar_keys(self, key, t):
        a = []
        q = deque()
        q.append(self)
        while len(q) != 0:
            current = q.popleft()
            d = damerau_lev(current.key, key)
            if d <= t:
                score = similarity_score(key, current.key)
                a.extend([(score, w) for w in current.words])
            lo, hi = max(0, d - t), d + t
            for j in range(lo, hi + 1):
                child = current.children.get(j, None)
                if child is not None:
                    q.append(child)
        return a

class BKTree:
    def __init__(self, t, w):
        self.tolerance = t
        self.words = {w}
        self.root = _Node(w)

    def add_word(self, w):
        if w in self.words:
            return
        self.words.add(w)
        self.root.add_word(w)

    def contains(self, w):
        return w in self.words

    def get_suggestions(self, w, n):
        s = strip_tones(w)
        a = self.root.words_with_similar_keys(s, self.tolerance)
        a.sort(reverse=True)
        return [t[1] for t in islice(a, 0, n)]
