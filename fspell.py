from bktree import BKTree

def get_words():
    lines = []
    with open("./words", "r", encoding="utf-8") as f:
        lines.extend(l[:-1] for l in f.readlines())
    return lines

def get_misspells():
    lines = []
    with open("./misspells", "r", encoding="utf-8") as f:
        lines.extend(l[:-1] for l in f.readlines())
    return lines

words = get_words()
mispells = get_misspells()
tree = BKTree(4, "")
for w in words:
    tree.add_word(w)

for s in mispells:
    a = tree.get_suggestions(s, 10)
    print("{}: {}".format(s, ", ".join(a)))
