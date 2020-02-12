from unicodedata import normalize, category

def strip_tones(word):
    """Remove tones form a word"""
    s = normalize("NFD", word)
    return "".join(c for c in s if category(c) != "Mn")
