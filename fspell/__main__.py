from .bktree import BKTree

MAX_EDIT_DISTANCE = 3

def get_words():
    lines = []
    with open("./words", "r", encoding="utf-8") as f:
        lines.extend(l.strip() for l in f)
    return lines

def get_misspells():
    lines = []
    with open("./misspells", "r", encoding="utf-8") as f:
        lines.extend(l.strip() for l in f)
    return lines

words = get_words()
mispells = get_misspells()
tree = BKTree(MAX_EDIT_DISTANCE, "")
for w in words:
    tree.add_word(w)

for s in mispells:
    a = tree.get_suggestions(s, 10)
    print("{}: {}".format(s, ", ".join(a)))
