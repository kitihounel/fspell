from unicodedata import normalize, category

def strip_tones(w):
    """Removes tones form a word."""
    s = normalize("NFD", w)
    return "".join(c for c in s if category(c) != "Mn")
